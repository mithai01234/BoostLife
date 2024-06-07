from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Otp, Address
class CustomUserAdmin(UserAdmin):
    list_display = ('email','status', 'name', 'is_active', 'is_staff','gender','age','height','weight','activity_level','goal')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('phone_number', 'name', 'referral_code','gender','age','height','weight','activity_level','goal')
    ordering = ('phone_number',)

    fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'password','status')}),
        ('Personal Info', {'fields': ('name', 'level','profile_photo','bio','gender','age','height','weight','activity_level','goal')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'name', 'email','referral_code', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Otp)
admin.site.register(Address)