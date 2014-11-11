from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from brasilcomvc.common.views import AnonymousRequiredMixin

from .forms import SignupForm


class Signup(AnonymousRequiredMixin, CreateView):
    '''
    User Signup
    '''

    form_class = SignupForm
    success_url = reverse_lazy('signup')
    template_name = 'accounts/signup.html'
