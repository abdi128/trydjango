from .models import Article
from django import forms


class ArticleForm(forms.Form):  
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        return title
