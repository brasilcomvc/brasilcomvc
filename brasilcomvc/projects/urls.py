from django.conf.urls import url

from .views import (
    ProjectDetails,
    ProjectList,
)


urlpatterns = (
    # Project List
    url(r'^$',
        ProjectList.as_view(), name='project_list'),

    # Project Details
    url(r'^(?P<slug>[\w-]+)/$',
        ProjectDetails.as_view(), name='project_details'),
)
