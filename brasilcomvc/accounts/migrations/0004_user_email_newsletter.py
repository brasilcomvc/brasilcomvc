# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user__bio__job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_newsletter',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
