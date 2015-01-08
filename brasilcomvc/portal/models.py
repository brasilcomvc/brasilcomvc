# coding: utf8
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def project_img_upload_to(instance, filename):
    return 'homebanners/{}/image.jpeg'.format(instance.id)


class HomeBanner(models.Model):

    image = ProcessedImageField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(1400, 550)],
        upload_to=project_img_upload_to)
    content = models.TextField()

    image.verbose_name = 'imagem'
    image.help_text = 'Imagem de alta resolução; será cortada para 1400x550.'
    content.verbose_name = 'conteúdo'
    content.help_text = 'Conteúdo (HTML) para sobrepor a imagem no banner.'
