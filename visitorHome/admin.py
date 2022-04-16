from django.contrib import admin
from . models import ExtendUser

# Register your models here.

@admin.register(ExtendUser)
class ExtendUserAdmin(admin.ModelAdmin):
    list_display= ['user','first_name','last_name','gender','email','profile','slug','is_active','created','updated'] 
    list_filter = ['user']
    prepopulated_fields = {'slug':('user',)}   
