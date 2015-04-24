from django.conf.urls import url
from django.views.generic import TemplateView

from .views import blog_redirect


urlpatterns = [
    # About
    url(r'^sobre/$',
        TemplateView.as_view(template_name='portal/about.html'), name='about'),

    # How It Works
    url(r'^como-funciona/$',
        TemplateView.as_view(template_name='portal/how_it_works.html'),
        name='how_it_works'),

    # Blog redirect
    url(r'^blog/$', blog_redirect, name='blog_redirect'),
]
