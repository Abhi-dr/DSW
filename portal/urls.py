from django.urls import path
from . import views, dean_views, cfo_views, club_views


urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    
    path('dean_home', dean_views.dean_home, name="dean_home"),
    path('dean_home/complaint', dean_views.complaint, name="complaint"),
    path('dean_home/events', dean_views.events, name="events"),
    path('dean_home/achievements', dean_views.achievements, name="achievements"),
    
    path('cfo_home', cfo_views.cfo_home, name="cfo_home"),
    path('cfo_home/events', cfo_views.events, name="cfo_events"),
    
    path('club_home', club_views.club_home, name="club_home"),
    path('club_home/events', club_views.events, name="club_events"),
    

]