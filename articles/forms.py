from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = []

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains = title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already taken. Try again")
        return data


"""class ArticleFormOld(forms.Form):  
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
"""