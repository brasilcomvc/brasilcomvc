from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import logout as logout_user
from django.contrib.auth.views import login as auth_login
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView


from brasilcomvc.common.views import AnonymousRequiredMixin, LoginRequiredMixin

from .forms import LoginForm, SignupForm


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
