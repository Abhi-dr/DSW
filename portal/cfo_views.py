from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def is_cfo(user):
    return user.is_cfo

@login_required(login_url='login')
def cfo_home(request):
    
    if is_cfo(request.user.member):
        return render(request, 'portal/cfo/home.html')
    
    return redirect("login")

@login_required(login_url='login')
def events(request):
    
    if is_cfo(request.user.member):
        return render(request, 'portal/cfo/events.html')
    
    return redirect("login")