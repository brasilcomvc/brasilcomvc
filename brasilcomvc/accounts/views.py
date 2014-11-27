from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import logout as logout_user
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import login as auth_login
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    TemplateView,
    UpdateView,
)


from brasilcomvc.common.views import AnonymousRequiredMixin, LoginRequiredMixin

from .forms import LoginForm, SignupForm, UserAddressForm


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class Signup(AnonymousRequiredMixin, CreateView):
    '''
    User Signup
    '''

    form_class = SignupForm
    success_url = reverse_lazy('signup')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        response = super(Signup, self).form_valid(form)
        self.object.send_welcome_email()  # Send welcome email upon signup
        return response


def login(request, *args, **kwargs):
    if request.user and request.user.is_authenticated():
        return HttpResponseRedirect(reverse('profile'))
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
    return HttpResponseRedirect(reverse('login'))


class BaseEditUser(LoginRequiredMixin):
    '''
    Base class for User Edit views.
    '''

    success_url = reverse_lazy('edit_dashboard')

    def get_object(self):
        return self.request.user


class EditDashboard(BaseEditUser, DetailView):

    template_name = 'accounts/edit_dashboard.html'


class EditPersonalInfo(BaseEditUser, UpdateView):

    template_name = 'accounts/edit_personal_info.html'
    fields = ('full_name', 'username', 'email',)


class EditProfessionalInfo(BaseEditUser, UpdateView):

    template_name = 'accounts/edit_professional_info.html'
    fields = ('job_title', 'bio',)


class EditNotifications(BaseEditUser, UpdateView):

    fields = ('email_newsletter',)
    template_name = 'accounts/edit_notifications.html'


class EditSecuritySettings(BaseEditUser, FormView):

    form_class = PasswordChangeForm
    template_name = 'accounts/edit_security_settings.html'

    def get_form_kwargs(self):
        return dict(
            super(EditSecuritySettings, self).get_form_kwargs(),
            user=self.get_object())

    def form_valid(self, form):
        form.save()
        return super(EditSecuritySettings, self).form_valid(form)


class EditUserAddress(BaseEditUser, FormView):

    form_class = UserAddressForm
    template_name = 'accounts/edit_user_address.html'

    def get_form_kwargs(self):
        return dict(
            super(EditUserAddress, self).get_form_kwargs(),

            # If the user already has an address, make it the edition target
            instance=getattr(self.request.user, 'address', None))

    def form_valid(self, form):
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        return super(EditUserAddress, self).form_valid(form)
