# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_project_latlng_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latlng',
            field=django.contrib.gis.db.models.fields.PointField(editable=False, db_index=True, null=True, srid=4326),
            preserve_default=True,
        ),
    ]
