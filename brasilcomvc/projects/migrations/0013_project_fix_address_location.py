# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_project_address_and_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.TextField(verbose_name='endereço'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.TextField(verbose_name='local', help_text='Local ou cidade. E.g. "Teatro Municipal" ou "São Paulo, SP".'),
            preserve_default=True,
        ),
    ]
