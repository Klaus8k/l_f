from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ['user', 'phone_number', 'telegram', 'adress',]
    # raw_id_fields = ['user']
