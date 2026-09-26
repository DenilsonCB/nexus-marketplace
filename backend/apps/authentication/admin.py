from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom administration panel for the User model.
    Extends the default UserAdmin to include custom profile fields.
    """
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Profile', {
            'fields': ('is_merchant', 'is_customer', 'phone_number'),
        }),
    )
    
    list_display = ('email', 'username', 'is_merchant', 'is_customer', 'is_staff')
    search_fields = ('email', 'username')