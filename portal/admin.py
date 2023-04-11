from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("username", "roll_no", "year", "phone_number", "is_dean", "is_cfo", "is_club_mentor")
    exclude = ('is_active', 'groups', 'user_permissions', 'password', 'is_staff', 'is_superuser', 'date_joined')
