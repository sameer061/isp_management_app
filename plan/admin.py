from django.contrib import admin
from .models import Plan,Userprofile
from import_export.admin import  ImportExportModelAdmin
# Register your models here.
class importexport(ImportExportModelAdmin,admin.ModelAdmin):
    pass

@admin.register(Plan)
class PLAN(importexport):
    list_display = (
       'plan_name',
        'description',
        'Duration',
        'cost',

    )

@admin.register(Userprofile)
class USER(importexport):
    list_display = (
        'user', 
        'first_name',
        'last_name',
        'address',
        'email',
        'profile_image',
        'current_plan',
        'phoneno',
        'start_date',
        'end_date'
    )
