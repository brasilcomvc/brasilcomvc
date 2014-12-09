# coding: utf8
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, UserAddress


class UserAdmin(admin.ModelAdmin):

    class UserAddressInline(admin.StackedInline):
        model = UserAddress

    list_display = ('email', 'full_name', 'username',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('full_name', 'username', 'email',),
        }),
        ('Informações Profissionais', {
            'fields': ('job_title', 'bio',),
        }),
        ('Notificações', {
            'fields': ('email_newsletter',),
        }),
    )
    inlines = (UserAddressInline,)


admin.site.register(User, UserAdmin)
