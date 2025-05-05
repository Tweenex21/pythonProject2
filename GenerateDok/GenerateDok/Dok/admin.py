from django.contrib import admin
from .models import DocumentTemplate, GeneratedDocument

@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    search_fields = ('name',)

@admin.register(GeneratedDocument)
class GeneratedDocumentAdmin(admin.ModelAdmin):
    list_display = ('template', 'created_at')
    list_filter = ('created_at',)