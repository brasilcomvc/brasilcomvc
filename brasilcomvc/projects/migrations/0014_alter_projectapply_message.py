# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_project_fix_address_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectapply',
            name='message',
            field=models.TextField(help_text='Conte-nos brevemente como você pode ajudar.'),
            preserve_default=True,
        ),
    ]
