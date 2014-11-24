# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from cities_light.models import City, Region

from .models import UserAddress


class LoginForm(AuthenticationForm):

    # this is named username so we can use Django's login view
    username = forms.EmailField(required=True)


class SignupForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('full_name', 'email',)

    def save(self, **kwargs):
        # Set password from user input
        self.instance.set_password(self.cleaned_data['password'])

        return super(SignupForm, self).save(**kwargs)


class SecuritySettingsForm(PasswordChangeForm):
    pass


class UserAddressForm(forms.ModelForm):

    class Meta:
        model = UserAddress
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)

        # Limit regions to available cities
        self.fields['state'].queryset = Region.objects.filter(
            id__in=set(City.objects.values_list('region_id', flat=True)))
