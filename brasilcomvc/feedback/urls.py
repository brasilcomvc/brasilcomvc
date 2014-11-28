from django.conf.urls import url

from .views import (
    Create,
    Confirm,
)


urlpatterns = (
    # Feedback Confirm
    url(r'obrigado/$',
        Confirm.as_view(), name='confirm'),

    # Feedback Create
    url(r'$',
        Create.as_view(), name='create'),
)
