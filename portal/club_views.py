from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def is_club(user):
    return user.is_club_mentor

@login_required(login_url='login')
def club_home(request):
    
    if is_club(request.user.member):
        return render(request, 'portal/club/home.html')
    
    return redirect("login")

@login_required(login_url='login')
def events(request):
    
    if is_club(request.user.member):
        return render(request, 'portal/club/events.html')
    
    return redirect("login")