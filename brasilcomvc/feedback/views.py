from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import FeedbackForm


class Create(CreateView):

    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:confirm')
    template_name = 'feedback/create.html'

    def form_valid(self, form):
        self.request.session.pop('deleted_email')
        return super(Create, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(Create, self).get_form_kwargs()
        if 'data' in kwargs:
            kwargs['data']._mutable = True
            kwargs['data'].update({
                'email': self.request.session['deleted_email'],
            })
        return kwargs


class Confirm(TemplateView):
    template_name = 'feedback/confirm.html'
