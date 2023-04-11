from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def is_dean(user):
    return user.is_dean


@login_required(login_url='login')
def dean_home(request):
    
    if is_dean(request.user.member):
        return render(request, 'portal/dean/home.html')
    
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