from django.conf.urls import url

from .views import (
    Create,
)


urlpatterns = (
    # Feedback Create
    url(r'$',
        Create.as_view(), name='create'),
)
