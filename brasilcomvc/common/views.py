from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class LoginRequiredMixin(object):

    '''
    Bind login requirement to any view
    '''

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AnonymousRequiredMixin(object):

    '''
    Make any view be accessible by unauthenticated users only
    '''

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super(AnonymousRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class UIGuidelineView(TemplateView):

    template_name = 'ui.html'

    class ExampleForm(forms.Form):
        '''
        A dummy form to represent every possible kind of form widget to be used
        in this project.
        '''

        _choices = [(1, 'One'), (2, 'Two'), (3, 'Three')]

        email = forms.EmailField(
            widget=forms.EmailInput())
        text = forms.CharField(
            widget=forms.TextInput(), min_length=3, max_length=10)
        text_disabled = forms.CharField(
            widget=forms.TextInput(attrs={'disabled': True}),
            help_text='Disabled just because.',
            initial='Immutable')
        textarea = forms.CharField(
            widget=forms.Textarea(
                attrs={'placeholder': 'Type something here'}))
        search = forms.CharField(
            widget=forms.TextInput(attrs={'type': 'search'}))
        one_choice_select = forms.IntegerField(
            widget=forms.Select(choices=_choices))
        one_choice_radio = forms.IntegerField(
            widget=forms.RadioSelect(choices=_choices))
        multi_choice_select = forms.IntegerField(
            widget=forms.SelectMultiple(choices=_choices))
        multi_choice_checkboxes = forms.IntegerField(
            widget=forms.CheckboxSelectMultiple(choices=_choices),
            help_text='Pick multiple options.')
        option_toggle = forms.BooleanField(
            widget=forms.CheckboxInput())
        option_toggle_disabled = forms.BooleanField(
            widget=forms.CheckboxInput(attrs={'disabled': True}))
        spin_number = forms.IntegerField(
            widget=forms.NumberInput(), initial=0)
        range_number = forms.IntegerField(
            widget=forms.NumberInput(
                attrs={'type': 'range', 'min': 0, 'max': 10, 'step': 1}),
            initial=0)
        date = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}))

    def get_context_data(self, **kwargs):
        return dict(
            super(UIGuidelineView, self).get_context_data(**kwargs),
            form=UIGuidelineView.ExampleForm(data={}),
        )
