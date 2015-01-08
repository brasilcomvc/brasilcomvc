from django import forms
from django.contrib import admin
from django.contrib.gis.db import models

from .models import (
    Project,
    Tag,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {'widget': forms.TextInput},
    }


admin.site.register(Tag)
