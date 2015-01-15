# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import groupby

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm as djangoPasswordResetForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from brasilcomvc.common.email import send_template_email
from cities_light.models import City, Region

from .models import UserAddress


User = get_user_model()


class DeleteUserForm(forms.Form):

    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        super(DeleteUserForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data['password']
        if not self.user.check_password(password):
            self.add_error('password', 'Senha inválida')
        return password


class LoginForm(AuthenticationForm):

    # this is named username so we can use Django's login view
    username = forms.EmailField(required=True)


class PasswordResetForm(djangoPasswordResetForm):
    '''
    Override the built-in form to customize email sending
    '''

    def save(
            self, use_https=False, token_generator=default_token_generator,
            from_email=None, domain_override=None, request=None, **kwargs):
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return

        if not user.has_usable_password():
            return

        if domain_override:
            site_name = domain = domain_override
        else:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain

        context = {
            'email': user.email,
            'domain': domain,
            'site_name': site_name,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': token_generator.make_token(user),
            'protocol': 'https' if use_https else 'http',
        }
        context['reset_link'] = '{protocol}://{domain}{url}'.format(
            url=reverse('accounts:password_reset_confirm', kwargs={
                'uidb64': context['uid'], 'token': context['token']}),
            **context)

        send_template_email(
            subject='Redefinição de senha',
            to=self.cleaned_data['email'],
            template_name='emails/password_reset.html',
            context=context)


class SignupForm(forms.ModelForm):

    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    def save(self, **kwargs):
        # Set password from user input
        self.instance.set_password(self.cleaned_data['password'])
        return super(SignupForm, self).save(**kwargs)


class EditNotificationsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email_newsletter',)
        labels = {
            'email_newsletter': 'Receber novidades sobre o Brasil.com.vc',
        }


class UserAddressForm(forms.ModelForm):

    class Meta:
        model = UserAddress
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)

        # Limit regions to available cities
        states = Region.objects.filter(
            id__in=set(City.objects.values_list('region_id', flat=True)))
        self.fields['state'].queryset = states
        self.fields['state'].choices = states.values_list('id', 'name')

        # Group cities by region (state)
        self.fields['city'].choices = self._group_cities()

    def _group_cities(self):
        '''
        Build a choices-like list with all cities grouped by state (region)
        '''
        return [
            (state, [(city.pk, city.name) for city in cities],)
            for state, cities in groupby(
                self.fields['city'].queryset.order_by('region__name', 'name'),
                lambda city: city.region.name)]
