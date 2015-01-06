# coding: utf8
from __future__ import unicode_literals

from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView

from brasilcomvc.common.views import LoginRequiredMixin

from .forms import ProjectApplyForm
from .models import Project


class ProjectList(ListView):

    template_name = 'projects/project_list.html'

    def get_queryset(self):
        return Project.objects.annotate(
            application_count=Count('applications'))


class ProjectDetails(DetailView):

    model = Project
    template_name = 'projects/project_details.html'

    def get_context_data(self, **kwargs):
        user = self.request.user

        return dict(
            super(ProjectDetails, self).get_context_data(**kwargs),
            user_is_participating=(
                user.is_authenticated() and
                self.object.applications.filter(volunteer=user).exists()))


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

        # Send emails to the involved parts
        application.send_owner_email()
        application.send_volunteer_email()

        # Display a message
        messages.success(
            self.request,
            'Inscrição realizada com sucesso! Você agora está participando '
            'deste projeto.')

        return super(ProjectApply, self).form_valid(form)

    def get_context_data(self, **kwargs):
        return dict(
            super(ProjectApply, self).get_context_data(**kwargs),
            project=self.get_project())
