# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import brasilcomvc.projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_tag_may_be_blank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
    ]
