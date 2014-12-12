from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView

from brasilcomvc.common.views import LoginRequiredMixin

from .forms import ProjectApplyForm
from .models import Project


class ProjectList(ListView):

    model = Project
    template_name = 'projects/project_list.html'


class ProjectDetails(DetailView):

    model = Project
    template_name = 'projects/project_details.html'


class ProjectApply(LoginRequiredMixin, CreateView):

    form_class = ProjectApplyForm
    template_name = 'projects/project_apply.html'

    def get_project(self):
        return get_object_or_404(Project, slug=self.kwargs['slug'])

    def get_form_kwargs(self):
        return dict(
            super(ProjectApply, self).get_form_kwargs(),
            volunteer=self.request.user,
            project=self.get_project())

    def get_success_url(self):
        return self.get_project().get_absolute_url()

    def form_valid(self, form):
        application = form.save(commit=False)
        application.project = form.project
        application.volunteer = form.volunteer
        application.save()

        return super(ProjectApply, self).form_valid(form)
