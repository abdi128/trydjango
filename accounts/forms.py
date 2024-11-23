from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []

    def clean(self):
        data = self.cleaned_data
        return data