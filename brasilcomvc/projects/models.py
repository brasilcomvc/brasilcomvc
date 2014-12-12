# coding: utf8
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible
from django.utils.text import slugify
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


def project_img_upload_to(instance, filename):
    return 'projects/{}/img.jpeg'.format(instance.slug)


@python_2_unicode_compatible
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
    agenda = models.TextField(default='', blank=True)
    img = ProcessedImageField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(854, 480)],
        upload_to=project_img_upload_to)
    img_thumbnail = ImageSpecField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(320, 240)],
        source='img')
    video = models.URLField(null=True, blank=True)

    name.verbose_name = 'nome'
    relevant_fact.verbose_name = 'fato relevante'
    about.verbose_name = 'descrição'
    short_description.verbose_name = 'descrição curta'
    how_to_help.verbose_name = 'como ajudar'
    requirements.verbose_name = 'requisitos'
    video.verbose_name = 'vídeo'

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project_details', kwargs={'slug': self.slug})

    def save(self, **kwargs):
        if self.pk is None:
            self.slug = slugify(smart_text(self.name))
        super(Project, self).save(**kwargs)


@python_2_unicode_compatible
class Tag(models.Model):

    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name
