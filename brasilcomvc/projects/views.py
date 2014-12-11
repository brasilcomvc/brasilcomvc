from django.views.generic import DetailView, ListView

from .models import Project


class ProjectList(ListView):

    model = Project
    template_name = 'projects/project_list.html'


class ProjectDetails(DetailView):

    model = Project
    template_name = 'projects/project_details.html'
