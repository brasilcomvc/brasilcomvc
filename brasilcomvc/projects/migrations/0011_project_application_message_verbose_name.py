# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_requirements_may_be_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectapply',
            name='message',
            field=models.TextField(verbose_name='Conte-nos brevemente como voc\xea pode nos ajudar'),
            preserve_default=True,
        ),
    ]
