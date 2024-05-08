from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('nombre_usuario', 'email', 'password')}),
        ('Personal info', {'fields': ('cumpleaños',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre_usuario', 'email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    list_display = ['nombre_usuario', 'email', 'is_staff', 'is_active']
    search_fields = ('nombre_usuario', 'email')
    ordering = ('nombre_usuario', 'email')

admin.site.register(User, CustomUserAdmin)
