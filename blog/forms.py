from django import forms

from .models import Blog

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter title'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'materialize-textarea',
                'placeholder': 'Enter blog content'
            }
        )
    )
    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
            'active'
        ]