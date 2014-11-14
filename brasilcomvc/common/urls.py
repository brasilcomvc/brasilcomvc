from django.conf.urls import url

from .views import UIGuidelineView


urlpatterns = [
    # UI Guideline
    url(r'^ui/$',
        UIGuidelineView.as_view(), name='ui'),
]
