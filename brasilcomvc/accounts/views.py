# coding: utf8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import (
    login as auth_login,
    password_reset as django_password_reset,
    password_reset_done as django_password_reset_done,
    password_reset_confirm as django_password_reset_confirm,
)
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    TemplateView,
    UpdateView,
)

from brasilcomvc.common.views import AnonymousRequiredMixin, LoginRequiredMixin

from .forms import (
    EditNotificationsForm,
    DeleteUserForm,
    LoginForm,
    PasswordResetForm,
    SignupForm,
    UserAddressForm,
)


class Signup(AnonymousRequiredMixin, CreateView):
    '''
    User Signup
    '''

    form_class = SignupForm
    success_url = reverse_lazy('accounts:edit_dashboard')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        response = super(Signup, self).form_valid(form)

        # log user in
        user = authenticate(email=form.cleaned_data['email'],
                            password=form.cleaned_data['password'])
        login_user(self.request, user)

        # Send welcome email upon signup
        user.send_welcome_email()

        # Display a welcome message
        messages.info(
            self.request,
            'Parabéns! Você agora está cadastrado e já pode buscar projetos '
            'para participar. Bem vindo e mãos à obra!')

        return response


def login(request, *args, **kwargs):
    if request.user and request.user.is_authenticated():
        return HttpResponseRedirect(reverse('accounts:edit_dashboard'))
    return auth_login(
        request,
        authentication_form=LoginForm,
        template_name='accounts/login.html',
    )


def logout(request):
    """
    Logout user and redirect back to login page
    """
    logout_user(request)
    return HttpResponseRedirect(reverse('accounts:login'))


def password_reset(request):
    return django_password_reset(
        request,
        template_name='accounts/password_reset.html',
        password_reset_form=PasswordResetForm,
        post_reset_redirect=reverse('accounts:password_reset_sent'))


def password_reset_sent(request):
    return django_password_reset_done(
        request,
        template_name='accounts/password_reset_sent.html')


def password_reset_confirm(request, **kwargs):
    return django_password_reset_confirm(
        request,
        template_name='accounts/password_reset_confirm.html',
        post_reset_redirect=reverse('accounts:login'),
        **kwargs)


class BaseEditUser(LoginRequiredMixin):
    '''
    Base class for User Edit views.
    '''

    success_message = 'Dados alterados com sucesso!'
    success_url = reverse_lazy('accounts:edit_dashboard')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(BaseEditUser, self).form_valid(form)


class EditDashboard(BaseEditUser, DetailView):

    template_name = 'accounts/edit_dashboard.html'


class EditPersonalInfo(BaseEditUser, UpdateView):

    template_name = 'accounts/edit_personal_info.html'
    fields = ('full_name', 'username', 'email', 'picture',)


class EditProfessionalInfo(BaseEditUser, UpdateView):

    template_name = 'accounts/edit_professional_info.html'
    fields = ('job_title', 'bio',)


class EditNotifications(BaseEditUser, UpdateView):

    form_class = EditNotificationsForm
    template_name = 'accounts/edit_notifications.html'


class EditSecuritySettings(BaseEditUser, UpdateView):

    form_class = PasswordChangeForm
    success_message = 'Configurações de segurança atualizadas com sucesso!'
    template_name = 'accounts/edit_security_settings.html'

    def get_form_kwargs(self):
        kwargs = super(EditSecuritySettings, self).get_form_kwargs()
        kwargs['user'] = kwargs.pop('instance')
        return kwargs


class EditUserAddress(BaseEditUser, UpdateView):

    form_class = UserAddressForm
    template_name = 'accounts/edit_user_address.html'

    def get_object(self):
        # If the user already has an address, make it the edition target
        return getattr(self.request.user, 'address', None)

    def form_valid(self, form):
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        return super(EditUserAddress, self).form_valid(form)


class DeleteUser(LoginRequiredMixin, FormView):

    form_class = DeleteUserForm
    template_name = 'accounts/delete-user.html'

    def get_form_kwargs(self):
        kwargs = super(DeleteUser, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        email = self.request.user.email

        # Delete user and logout (clean session)
        self.request.user.delete()
        logout_user(self.request)

        # Put deleted_email into session for feedback form consumption
        self.request.session['deleted_email'] = email
        self.request.session['feedback_success_message'] = (
            'Sua conta foi excluída. Até logo! :(')
        return HttpResponseRedirect('{}?next={}'.format(
            reverse('feedback:create'), reverse('accounts:login')))
