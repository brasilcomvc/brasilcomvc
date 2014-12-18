# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_project_application_message_verbose_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Endere\xe7o'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(default='', help_text='Nome do local ou cidade/UF. E.g. Teatro Municipal ou S\xe3o Paulo, SP', max_length=255, verbose_name='Local'),
            preserve_default=False,
        ),
    ]
