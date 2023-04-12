from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from achievement.models import Achievement
from django.contrib import messages


def is_dean(user):
    return user.is_dean


@login_required(login_url='login')
def dean_home(request):
    
    if is_dean(request.user.member):
        
        achievements = Achievement.objects.filter(is_approved=False, is_rejected=False)
        
        
        parameters = {
            'achievements': achievements,
        }
        
        return render(request, 'portal/dean/home.html', parameters)
    
    return redirect("login")

@login_required(login_url='login')
def complaint(request):
    if is_dean(request.user.member):
        return render(request, 'portal/dean/complaint.html')

    return redirect("login")

@login_required(login_url='login')
def events(request):
    if is_dean(request.user.member):
        return render(request, 'portal/dean/events.html')
    
    return redirect("login")

@login_required(login_url='login')
def achievements(request):
    
    if is_dean(request.user.member):
        return render(request, 'portal/dean/achievements.html')
    
    return redirect("login")

# ======================================= APPROVE ACHIEVEMENT =======================================

@login_required(login_url='login')
def approve_achievement(request, id):
    
    if is_dean(request.user.member):
        
        achievement = Achievement.objects.get(id = id)
        
        achievement.is_approved = True
        
        achievement.save()
        
        messages.request(request, 'Achievement Approved')
        
        return redirect('dean_home')
        
        
    
    return redirect("login")
