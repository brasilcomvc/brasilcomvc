# coding: utf8
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Project(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='projects_owned')
    name = models.CharField(max_length=60)
    relevant_fact = models.TextField(null=True, blank=True)
    about = models.TextField()
    short_description = models.TextField(null=True, blank=True)
    how_to_help = models.TextField()
    requirements = models.TextField()

    name.verbose_name = 'nome'
    relevant_fact.verbose_name = 'fato relevante'
    about.verbose_name = 'descrição'
    short_description.verbose_name = 'descrição curta'
    how_to_help.verbose_name = 'como ajudar'
    requirements.verbose_name = 'requisitos'
