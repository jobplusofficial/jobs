from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(Visitors)
admin.site.register(Categary_label)
@admin.register(Job)
class JobsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'company_name','profile_name','looking_for')
    search_fields = ("id__startswith", )
    
    pass
@admin.register(Catagories)
class JobsAdmin(ImportExportModelAdmin):
    # search_fields = ("id__startswith",)
    search_fields = ("catagory",)
    pass
@admin.register(Courses_and_certification)
class JobsAdmin(ImportExportModelAdmin):
    pass
  