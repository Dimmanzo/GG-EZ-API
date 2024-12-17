from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register the Custom user role in the admin panel.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
