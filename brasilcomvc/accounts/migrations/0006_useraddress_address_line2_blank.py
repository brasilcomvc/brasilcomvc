# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address_line2',
            field=models.CharField(blank=True, max_length=80),
            preserve_default=True,
        ),
    ]
