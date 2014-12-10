from django.views.generic import DetailView

from .models import Project


class ProjectDetails(DetailView):

    model = Project
    template_name = 'projects/project_details.html'
