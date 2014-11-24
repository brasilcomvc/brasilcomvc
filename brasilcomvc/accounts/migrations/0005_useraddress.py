# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0003_auto_20141124_1354'),
        ('accounts', '0004_user_email_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=90)),
                ('address_line1', models.CharField(max_length=120)),
                ('address_line2', models.CharField(max_length=80)),
                ('city', models.ForeignKey(to='cities_light.City')),
                ('state', models.ForeignKey(to='cities_light.Region')),
                ('user', models.OneToOneField(related_name='address', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
