# coding: utf8
from __future__ import unicode_literals

from django import forms

from .models import ProjectApply


class ProjectApplyForm(forms.ModelForm):

    class Meta:
        model = ProjectApply
        fields = ('message',)

    def __init__(self, volunteer, project, *args, **kwargs):
        self.volunteer = volunteer
        self.project = project
        super(ProjectApplyForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.volunteer == self.project.owner:
            raise forms.ValidationError(
                'Você não pode se inscrever no próprio projeto!')

        if self.project.applications.filter(volunteer=self.volunteer).exists():
            raise forms.ValidationError(
                'Você já está participando desse projeto.')


class ProjectSearchForm(forms.Form):
    lat = forms.FloatField()
    lng = forms.FloatField()
    q = forms.CharField()
    radius = forms.IntegerField(required=False)

    def clean_radius(self):
        cleaned_data = self.cleaned_data

        if 'radius' not in cleaned_data or not cleaned_data['radius']:
            return 30

        return cleaned_data['radius']
