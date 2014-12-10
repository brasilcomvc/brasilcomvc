from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/social/',
        include('social.apps.django_app.urls', namespace='social')),

    url(r'^feedback/',
        include('brasilcomvc.feedback.urls', namespace='feedback')),

    url(r'^guideline/',
        include('brasilcomvc.guideline.urls', namespace='guideline')),

    url(r'', include('brasilcomvc.accounts.urls')),

    url(r'', include('brasilcomvc.projects.urls', namespace='projects')),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns = list(urlpatterns) + static(settings.MEDIA_URL,
                                             document_root=settings.MEDIA_ROOT)
