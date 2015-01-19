# coding: utf8
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView

from brasilcomvc.common.views import LoginRequiredMixin
from brasilcomvc.portal.models import HomeBanner

from .forms import ProjectApplyForm, ProjectSearchForm
from .models import Project


class ProjectList(ListView):

    template_name = 'projects/project_list.html'

    def get_queryset(self):
        return Project.objects.annotate(
            application_count=Count('applications'))

    def get_context_data(self, **kwargs):
        return dict(
            super(ProjectList, self).get_context_data(**kwargs),
            banner=(HomeBanner.objects.order_by('?')[:1] or (None,))[0])


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


class ProjectSearch(ListView):

    context_object_name = 'projects'
    form_class = ProjectSearchForm
    template_name = 'projects/project_search.html'

    def get(self, request, *args, **kwargs):
        self.form = ProjectSearchForm(request.GET)
        return super(ListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProjectSearch, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get_queryset(self):
        projects = Project.objects.none()

        if self.form.is_valid():
            # Filter by distance
            lat = self.form.cleaned_data['lat']
            lng = self.form.cleaned_data['lng']
            radius = self.form.cleaned_data['radius'] or 30

            user_location = Point(lng, lat, srid=4326)
            projects = Project.objects.filter(
                latlng__distance_lte=(user_location, D(km=radius)))

        return projects
