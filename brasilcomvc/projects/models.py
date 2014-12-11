# coding: utf8
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import smart_text
from django.utils.text import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def project_img_upload_to(instance, filename):
    return 'projects/{}/img.jpeg'.format(instance.slug)


class Project(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='projects_owned')
    name = models.CharField(max_length=60)
    slug = models.SlugField(editable=False)
    relevant_fact = models.TextField(null=True, blank=True)
    about = models.TextField()
    short_description = models.TextField(null=True, blank=True)
    how_to_help = models.TextField()
    requirements = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    agenda = models.TextField(null=True, blank=True)
    img = ProcessedImageField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(640, 480)],
        upload_to=project_img_upload_to)

    name.verbose_name = 'nome'
    relevant_fact.verbose_name = 'fato relevante'
    about.verbose_name = 'descrição'
    short_description.verbose_name = 'descrição curta'
    how_to_help.verbose_name = 'como ajudar'
    requirements.verbose_name = 'requisitos'

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project_details', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        if self.pk is None:
            self.slug = slugify(smart_text(self.name))
        super(Project, self).save(**kwargs)


class Tag(models.Model):

    name = models.CharField(max_length=24)
