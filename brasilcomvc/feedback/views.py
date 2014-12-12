from django.views.generic import CreateView

from .forms import FeedbackForm


class Create(CreateView):

    form_class = FeedbackForm
    template_name = 'feedback/create.html'

    def get_success_url(self):
        return self.request.GET['next']

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
