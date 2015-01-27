# coding: utf8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import striptags, truncatechars
from django.utils.timezone import now
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def homebanner_image_upload_to(instance, filename):
    return 'homebanners/{:%Y-%m-%d}/image.jpeg'.format(instance.created)


def homebanner_video_upload_to(instance, filename):
    return 'homebanners/{created:%Y-%m-%d}/video{extension}'.format(
        created=instance.created,
        extension=filename[filename.rfind('.'):])


@python_2_unicode_compatible
class HomeBanner(models.Model):

    image = ProcessedImageField(
        format='JPEG',
        options={'quality': 90},
        processors=[ResizeToFill(2000, 550)],
        upload_to=homebanner_image_upload_to)
    video = models.FileField(
        null=True, blank=True, upload_to=homebanner_video_upload_to)
    content = models.TextField()
    created = models.DateTimeField(default=now, editable=False)

    image.verbose_name = 'imagem'
    image.help_text = 'Imagem de alta resolução; será cortada para 1400x550.'
    video.verbose_name = 'vídeo'
    video.help_text = 'Vídeo curto e leve; ficará em loop.'
    content.verbose_name = 'conteúdo'
    content.help_text = 'Conteúdo (HTML) para sobrepor a imagem no banner.'

    class Meta:
        verbose_name = 'Banner da Home'
        verbose_name_plural = 'Banners da Home'

    def __str__(self):
        return truncatechars(striptags(self.content), 40)
