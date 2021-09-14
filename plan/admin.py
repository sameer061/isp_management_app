from django.contrib import admin
from .models import Plan,Userprofile
# Register your models here.
@admin.register(Plan)
class PLAN(admin.ModelAdmin):
    list_display = ('plan_name','Duration','description')

@admin.register(Userprofile)
class USER(admin.ModelAdmin):
    list_display = (
        'user', 
        'first_name',
        'last_name',
        'address',
        'email',
        'profile_image',
        'phoneno',
        'start_date',
        'end_date'
    )