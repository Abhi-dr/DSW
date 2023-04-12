from django.contrib import admin
from .models import Dean_Message


@admin.register(Dean_Message)
class Dean_MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'complaint', 'date', 'is_replied', 'is_solved')
