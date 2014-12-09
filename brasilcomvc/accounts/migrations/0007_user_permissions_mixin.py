# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('accounts', '0006_useraddress_address_line2_blank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'usuário'},
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', blank=True, verbose_name='groups', related_query_name='user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', to='auth.Permission', blank=True, verbose_name='user permissions', related_query_name='user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Nome Completo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
            preserve_default=True,
        ),
    ]
