# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import brasilcomvc.portal.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', imagekit.models.fields.ProcessedImageField(help_text='Imagem de alta resolução; será cortada para 1400x550.', upload_to=brasilcomvc.portal.models.project_img_upload_to)),
                ('content', models.TextField(help_text='Conteúdo (HTML) para sobrepor a imagem no banner.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
