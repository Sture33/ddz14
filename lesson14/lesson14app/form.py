from django import forms

from lesson14app.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
     model = Feedback
     fields = ['name', 'email', 'text', 'tags']
     widgets = {
        'tags': forms.CheckboxSelectMultiple
     }







