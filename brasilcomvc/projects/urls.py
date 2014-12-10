from django.conf.urls import url

from .views import (
    ProjectDetails,
)


urlpatterns = (
    # Project Details
    url(r'^(?P<slug>[\w-]+)/$',
        ProjectDetails.as_view(), name='project_details'),
)
