# coding: utf8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_text, python_2_unicode_compatible
from django.utils.text import slugify
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from pygeocoder import Geocoder, GeocoderError

from brasilcomvc.common.email import send_template_email


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
    requirements = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    agenda = models.TextField(default='', blank=True)
    address = models.TextField(verbose_name='endereço')
    location = models.TextField(verbose_name='local', help_text=(
        'Local ou cidade. E.g. "Teatro Municipal" ou "São Paulo, SP".'))
    latlng = models.PointField(
        null=True, srid=4326, db_index=True, editable=False)

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
    img_opengraph = ImageSpecField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(800, 420)],
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

    def clean(self):
        # Use Google Maps API to geocode `address` into `latlng`
        try:
            addr = Geocoder.geocode(' '.join(self.address.splitlines()))[0]
            self.latlng = Point(y=addr.latitude, x=addr.longitude, srid=4326)

        except GeocoderError as err:
            if err.status != GeocoderError.G_GEO_ZERO_RESULTS:
                raise
            raise ValidationError('Endereço não reconhecido no Google Maps.')

    def save(self, **kwargs):
        if self.pk is None:
            self.slug = slugify(smart_text(self.name))
        super(Project, self).save(**kwargs)


@python_2_unicode_compatible
class Tag(models.Model):

    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProjectApply(models.Model):

    volunteer = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='applications', editable=False)
    project = models.ForeignKey(
        'Project', related_name='applications', editable=False)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    volunteer.verbose_name = 'voluntário'
    project.verbose_name = 'projeto'
    message.verbose_name = 'mensagem ao organizador'
    message.help_text = 'Conte-nos brevemente como você pode ajudar.'
    created.verbose_name = 'hora do registro'

    class Meta:
        unique_together = ('project', 'volunteer',)
        verbose_name = 'inscrição em projeto'
        verbose_name_plural = 'inscrições em projetos'

    def __str__(self):
        return '{}: {}'.format(self.project.name, self.volunteer.full_name)

    def _get_email_context(self):
        return {
            attr: getattr(self, attr)
            for attr in ('message', 'project', 'volunteer',)}

    def send_owner_email(self):
        send_template_email(
            subject='Alguém se inscreveu no seu projeto!',
            to=self.project.owner.email,
            template_name='emails/project_apply_owner.html',
            context=self._get_email_context())

    def send_volunteer_email(self):
        send_template_email(
            subject='Você se inscreveu num projeto!',
            to=self.volunteer.email,
            template_name='emails/project_apply_volunteer.html',
            context=self._get_email_context())
