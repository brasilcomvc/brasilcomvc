# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_homebanner_image_upload_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homebanner',
            options={'verbose_name_plural': 'Banners da Home', 'verbose_name': 'Banner da Home'},
        ),
    ]
