from django.contrib import admin
from .models import Company, Project, Role


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)
    
