from django.conf.urls import url

from .views import (
    Signup,
)


urlpatterns = (
    # User Signup
    url(r'^cadastro/$',
        Signup.as_view(), name='signup'),
)
