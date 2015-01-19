# coding: utf8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import striptags, truncatechars
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def project_img_upload_to(instance, filename):
    return 'homebanners/{}/image.jpeg'.format(instance.id)


@python_2_unicode_compatible
class HomeBanner(models.Model):

    image = ProcessedImageField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(1400, 550)],
        upload_to=project_img_upload_to)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    image.verbose_name = 'imagem'
    image.help_text = 'Imagem de alta resolução; será cortada para 1400x550.'
    content.verbose_name = 'conteúdo'
    content.help_text = 'Conteúdo (HTML) para sobrepor a imagem no banner.'

    class Meta:
        verbose_name = 'Banner da Home'
        verbose_name_plural = 'Banners da Home'

    def __str__(self):
        return truncatechars(striptags(self.content), 40)
