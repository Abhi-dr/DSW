from django.shortcuts import render


def achievement(request):
    return render(request, 'achievement.html')