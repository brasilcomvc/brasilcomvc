from django import forms


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
    password = forms.CharField(
        widget=forms.PasswordInput)
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
