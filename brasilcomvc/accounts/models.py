from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models


class User(AbstractBaseUser):

    # Identification
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    # Status
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(editable=False, default=True)
    is_staff = models.BooleanField(editable=False, default=False)
    is_superuser = models.BooleanField(editable=False, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    objects = UserManager()

    def get_short_name(self):
        return self.full_name.split(maxsplit=1)[0]

    def get_full_name(self):
        return self.full_name
