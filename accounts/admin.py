from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Location, HomeLocation

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'name',
        'surname',
        'phone_number', 
        'email',
        'username',
        'gender', 
        'access_levels',
    ]
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'surname', 'phone_number', 'gender', 'access_levels',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'name', 'surname', 'phone_number', 'gender', 'access_levels',)}),
    )


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = [
        'name',
        'constituency',
        'ward',
        'phone_number',
    ]

class HomeLocationAdmin(admin.ModelAdmin):
    model = HomeLocation
    list_display = [
        'home_address',
        'location',
        'owner_name',
        'phone_number',
    ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(HomeLocation, HomeLocationAdmin)