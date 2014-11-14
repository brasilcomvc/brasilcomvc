from django.conf.urls import url

from .views import (
    Profile,
    Signup,
)


urlpatterns = (
    # User Profile
    url(r'^profile/$',
        Profile.as_view(), name='profile'),

    # User Signup
    url(r'^cadastro/$',
        Signup.as_view(), name='signup'),
)
