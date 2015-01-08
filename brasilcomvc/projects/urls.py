from django.conf.urls import url

from .views import (
    ProjectApply,
    ProjectDetails,
    ProjectList,
    ProjectSearch,
)


urlpatterns = (
    # Project Search
    url(r'^busca/$',
        ProjectSearch.as_view(), name='project_search'),

    # Project List
    url(r'^$',
        ProjectList.as_view(), name='project_list'),

    # Project Details
    url(r'^(?P<slug>[\w-]+)/$',
        ProjectDetails.as_view(), name='project_details'),

    # Project Apply
    url(r'^(?P<slug>[\w-]+)/apply$',
        ProjectApply.as_view(), name='project_apply'),
)
