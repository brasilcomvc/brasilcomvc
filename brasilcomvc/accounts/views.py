from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView


from brasilcomvc.common.views import AnonymousRequiredMixin, LoginRequiredMixin

from .forms import SignupForm


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class Signup(AnonymousRequiredMixin, CreateView):
    '''
    User Signup
    '''

    form_class = SignupForm
    success_url = reverse_lazy('signup')
    template_name = 'accounts/signup.html'
