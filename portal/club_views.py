from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from event.models import Event, Club

def is_club(user):
    return user.is_club_mentor

@login_required(login_url='login')
def club_home(request):
    
    if is_club(request.user.member):
        
        club = Club.objects.get(factuly_incharge = request.user.member)
        unapproved_events = Event.objects.filter(club = club, is_approved_by_cfo=False)
        
        parameters = {
            "club": club,
            "unapproved_events": unapproved_events,
        }
        
        return render(request, 'portal/club/home.html', parameters)
    
    return redirect("login")

@login_required(login_url='login')
def events(request):
    
    if is_club(request.user.member):
        club = Club.objects.get(factuly_incharge = request.user.member)
        events = Event.objects.filter(club = club)
        
        
        parameters = {
            "club": club,
            "events": events,
        }
        
        return render(request, 'portal/club/events.html', parameters)
    
    return redirect("login")


#===================================================================================================

@login_required(login_url="login")
def delete_event(request, id):
    
    if is_club(request.user.member):
    
        event = Event.objects.get(id = id)
        event.delete()
        
        print("Event deleted successfuly!")
        
        return redirect("club_home")
    
    else:
        return redirect("login")