from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    # About
    url(r'^sobre/$',
        TemplateView.as_view(template_name='portal/about.html'), name='about'),

    # How It Works
    url(r'^como-funciona/$',
        TemplateView.as_view(template_name='portal/how_it_works.html'),
        name='how_it_works'),
]
