from django.urls import path
from . import views, dean_views, cfo_views, club_views


urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    
    path('dean_home', dean_views.dean_home, name="dean_home"),
    path('dean_home/complaint', dean_views.complaint, name="complaint"),
    path('dean_home/events', dean_views.events, name="events"),
    path('dean_home/achievements', dean_views.achievements, name="achievements"),
    
    path('approve_achievement/<int:id>', dean_views.approve_achievement, name="approve_achievement"),
    path('reject_achievement/<int:id>', dean_views.reject_achievement, name="reject_achievement"),
    
    path('approve_event/<int:id>', dean_views.approve_event, name="approve_event"),
    path('reject_event/<int:id>', dean_views.reject_event, name="reject_event"),
    
    # ================================================================================================
    
    path('cfo_home', cfo_views.cfo_home, name="cfo_home"),
    path('cfo_home/events', cfo_views.events, name="cfo_events"),
    
    path('cfo_approve_event/<int:id>', cfo_views.approve_event, name="cfo_approve_event"),
    path('cfo_reject_event/<int:id>', cfo_views.reject_event, name="cfo_reject_event"),
    
    # ================================================================================================
    
    path('club_home', club_views.club_home, name="club_home"),
    path('club_home/events', club_views.events, name="club_events"),
    
    path('delete_event/<int:id>', club_views.delete_event, name="delete_event"),
    
    
    

]


