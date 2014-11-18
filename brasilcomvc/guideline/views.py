from django.views.generic import TemplateView

from .forms import ExampleForm


class UIGuidelineView(TemplateView):

    template_name = 'guideline/ui.html'

    def get_context_data(self, **kwargs):
        return dict(
            super(UIGuidelineView, self).get_context_data(**kwargs),
            empty_form=ExampleForm(),
            invalid_form=ExampleForm(data={}),
        )
