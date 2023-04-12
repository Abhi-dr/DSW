from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from achievement.models import Achievement
from grivance.models import Dean_Message
from event.models import Event, Club
from django.contrib import messages


def is_dean(user):
    return user.is_dean


@login_required(login_url='login')
def dean_home(request):

    if is_dean(request.user.member):

        complaints = Dean_Message.objects.filter(
            is_solved=False, is_replied=False)
        unapproved_events = Event.objects.filter(is_approved_by_dean=False, is_rejected=False)
        unapproved_achievements = Achievement.objects.filter(
            is_approved=False, is_rejected=False)

        parameters = {
            'unapproved_achievements': unapproved_achievements,
            'complaints': complaints,
            'unapproved_events': unapproved_events,
        }

        return render(request, 'portal/dean/home.html', parameters)

    return redirect("login")


@login_required(login_url='login')
def complaint(request):
    if is_dean(request.user.member):

        complaints = Dean_Message.objects.filter()

        parameters = {
            "complaints": complaints,
        }

        return render(request, 'portal/dean/complaint.html', parameters)

    return redirect("login")


@login_required(login_url='login')
def events(request):
    if is_dean(request.user.member):

        events = Event.objects.all()

        parameters = {
            "events": events,
        }

        return render(request, 'portal/dean/events.html', parameters)

    return redirect("login")


@login_required(login_url='login')
def achievements(request):

    if is_dean(request.user.member):

        achievements = Achievement.objects.all()

        parameters = {
            "achievements": achievements,
        }

        return render(request, 'portal/dean/achievements.html', parameters)

    return redirect("login")

# ======================================= APPROVE ACHIEVEMENT =======================================


@login_required(login_url='login')
def approve_achievement(request, id):

    if is_dean(request.user.member):

        achievement = Achievement.objects.get(id=id)

        achievement.is_approved = True

        achievement.save()

        messages.success(request, 'Achievement Approved')

        return redirect('dean_home')

    return redirect("login")

# ======================================= REJECT ACHIEVEMENT =======================================


@login_required(login_url='login')
def reject_achievement(request, id):

    if is_dean(request.user.member):

        achievement = Achievement.objects.get(id=id)

        achievement.is_rejected = True

        achievement.save()

        messages.success(request, 'Achievement Rejected')

        return redirect('dean_home')

    return redirect("login")

# ===============================================================================================
# ===============================================================================================


@login_required(login_url='login')
def approve_event(request, id):

    if is_dean(request.user.member):

        event = Event.objects.get(id=id)

        event.is_approved_by_dean = True

        event.save()

        messages.success(request, 'Event Approved')

        return redirect('dean_home')

    return redirect("login")


@login_required(login_url='login')
def reject_event(request, id):
    
    if is_dean(request.user.member):

        event = Event.objects.get(id=id)

        event.is_rejected = True

        event.save()

        messages.success(request, 'Event Rejected')

        return redirect('dean_home')

    return redirect("login")