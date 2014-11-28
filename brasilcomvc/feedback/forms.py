from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        fields = [
            'email',
            'question_1',
            'question_2',
            'question_3',
            'question_4',
            'question_5',
            'comments',
        ]
        model = Feedback

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.HiddenInput()
        self.fields['comments'].required = False
