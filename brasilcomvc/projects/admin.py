from django import forms
from django.contrib import admin
from django.contrib.gis.db import models

from .models import (
    Project,
    ProjectApply,
    Tag,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {'widget': forms.TextInput},
    }


@admin.register(ProjectApply)
class ProjectApplyAdmin(admin.ModelAdmin):

    actions = None
    date_hierarchy = 'created'
    list_display = ('project', 'volunteer', 'created', 'message',)
    list_display_links = None
    list_filter = ('created',)
    search_fields = ('project__name', 'volunteer__full_name', 'message',)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Tag)
