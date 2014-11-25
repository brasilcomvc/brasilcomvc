# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=75)),
                ('question_1', models.BooleanField(default=False, verbose_name='Não recebi ou recebi poucos projetos próximos')),
                ('question_2', models.BooleanField(default=False, verbose_name='Não recebi ou recebi poucos projetos para meu perfil')),
                ('question_3', models.BooleanField(default=False, verbose_name='Recebo muitos e-mails do Brasil.com.vc')),
                ('question_4', models.BooleanField(default=False, verbose_name='Não tenho mais tempo para ajudar')),
                ('question_5', models.BooleanField(default=False, verbose_name='Não tenho mais tempo para pesquisar utilizando o serviço')),
                ('comments', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
