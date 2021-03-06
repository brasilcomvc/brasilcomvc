# encoding: utf8
from __future__ import unicode_literals

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from brasilcomvc.common.email import send_template_email


def user_picture_upload_to(instance, filename):
    return 'users/{}/picture.jpg'.format(instance.pk)


class UserManager(BaseUserManager):
    '''
    A custom manager class to provide user management that fits our model
    '''

    def create_user(self, email, password=None, **fields):
        user = User(email=email, **fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **fields):
        user = self.create_user(email, password, **fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    # Personal Info
    email = models.EmailField(unique=True)
    full_name = models.CharField('Nome Completo', max_length=255)
    username = models.SlugField(max_length=30, null=True, blank=True)
    picture = ProcessedImageField(
        null=True, blank=True,
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(256, 256)],
        upload_to=user_picture_upload_to)
    picture_medium = ImageSpecField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(128, 128)],
        source='picture')
    picture_small = ImageSpecField(
        format='JPEG',
        options={'quality': 80},
        processors=[ResizeToFill(50, 50)],
        source='picture')

    # Professional Info
    job_title = models.CharField(max_length=80, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # Status
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(editable=False, default=True)
    is_staff = models.BooleanField(editable=False, default=False)

    # Notifications
    email_newsletter = models.BooleanField(default=True)

    # Verbose names
    email.verbose_name = 'e-mail'
    full_name.verbose_name = 'nome completo'
    username.verbose_name = 'nome de usuário'
    picture.verbose_name = 'foto do usuário'
    job_title.verbose_name = 'profissão'
    bio.verbose_name = 'biografia'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    objects = UserManager()

    class Meta:
        verbose_name = 'usuário'

    def get_short_name(self):
        return self.full_name.split()[0] if self.full_name else ''

    def get_full_name(self):
        return self.full_name

    def send_welcome_email(self):
        send_template_email(
            subject='Bem vindo!',
            to=self.email,
            template_name='emails/welcome.html',
            context={'user': self})


class UserAddress(models.Model):

    user = models.OneToOneField('User', related_name='address', editable=False)
    zipcode = models.CharField(max_length=90)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=80, blank=True)
    state = models.ForeignKey('cities_light.Region')
    city = models.ForeignKey('cities_light.City')

    # Verbose names
    zipcode.verbose_name = 'CEP'
    address_line1.verbose_name = 'endereço'
    address_line2.verbose_name = 'complemento'
    state.verbose_name = 'estado'
    city.verbose_name = 'cidade'
