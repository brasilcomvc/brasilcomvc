# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_project_latlng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latlng',
            field=django.contrib.gis.db.models.fields.PointField(help_text='Formato: SRID=4326;POINT(longitude latitude)', srid=4326, null=True),
            preserve_default=True,
        ),
    ]
