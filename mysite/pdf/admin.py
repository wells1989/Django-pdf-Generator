from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'phone', 'degree', 'school', 'university', 'skills')


# Register your models here.
admin.site.register(Profile, ProfileAdmin)