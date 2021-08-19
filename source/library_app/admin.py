from django.contrib import admin
from .models import *

admin.site.site_header = ' '
admin.site.site_title = " "
admin.site.index_title = " "


# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    search_fields=['name', 'type', 'incident_type', 'section']
    list_display = ['name', 'type', 'incident_type', 'section', 'user', 'date', 'file']
    list_filter = ['date', 'type', 'section', 'user', 'incident_type',  'created_at','tags']
    readonly_fields = ['created_at']

    

    class Meta:
        model = Document

admin.site.register(Document, DocumentAdmin)