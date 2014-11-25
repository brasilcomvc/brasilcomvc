from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models

from brasilcomvc.common.email import send_template_email


class User(AbstractBaseUser):

    # Personal Info
    email = models.EmailField(unique=True)
    full_name = models.CharField('Nome Completo', max_length=255)
    username = models.SlugField(max_length=30, null=True, blank=True)

    # Professional Info
    job_title = models.CharField(max_length=80, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # Status
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(editable=False, default=True)
    is_staff = models.BooleanField(editable=False, default=False)
    is_superuser = models.BooleanField(editable=False, default=False)

    # Notifications
    email_newsletter = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    objects = UserManager()

    def get_short_name(self):
        return self.full_name.split(maxsplit=1)[0]

    def get_full_name(self):
        return self.full_name

    def send_welcome_email(self):
        send_template_email(
            subject='Bem vindo!',
            to=self.email,
            template_name='emails/welcome.html',
            context={'user': self})
