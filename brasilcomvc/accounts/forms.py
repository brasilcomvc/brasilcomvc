from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('full_name', 'email',)

    def save(self, **kwargs):
        # Set password from user input
        self.instance.set_password(self.cleaned_data['password'])

        return super(SignupForm, self).save(**kwargs)
