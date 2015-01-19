# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields
import brasilcomvc.portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_homebanner_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homebanner',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=brasilcomvc.portal.models.homebanner_image_upload_to, help_text='Imagem de alta resolução; será cortada para 1400x550.'),
            preserve_default=True,
        ),
    ]
