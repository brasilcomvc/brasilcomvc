from django.conf.urls import url

from django.views.generic import TemplateView


urlpatterns = [
    # UI Guideline
    url(r'^ui/$',
        TemplateView.as_view(template_name='ui.html'), name='ui'),
]
