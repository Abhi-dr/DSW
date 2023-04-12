from django.contrib import admin
from .models import Event, Club


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'organizer', 'date', 'venue', 'is_approved_by_dean', 'is_approved_by_cfo')
    
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'factuly_incharge', 'president', 'description')
