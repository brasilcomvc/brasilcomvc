# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import brasilcomvc.accounts.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_permissions_mixin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=brasilcomvc.accounts.models.user_picture_upload_to),
            preserve_default=True,
        ),
    ]
