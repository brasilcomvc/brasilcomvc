from __future__ import unicode_literals

from django.apps import AppConfig

from cities_light.signals import city_items_pre_import

from .signals import (
    filter_city_import,
)


class AccountsAppConfig(AppConfig):

    name = 'brasilcomvc.accounts'
    verbose_name = 'Usuários e autenticação'

    def ready(self):
        city_items_pre_import.connect(filter_city_import)
