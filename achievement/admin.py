from django.contrib import admin

from .models import Achievement, Header


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_approved', 'is_rejected')
