from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),

    url(r'^feedback/',
        include('brasilcomvc.feedback.urls', namespace='feedback')),

    url(r'^guideline/',
        include('brasilcomvc.guideline.urls', namespace='guideline')),

    url(r'', include('brasilcomvc.accounts.urls')),
)
