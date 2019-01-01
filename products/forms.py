from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class ValidatedProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : "Enter product name"
            }
        )
    )
    email = forms.EmailField()
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id': "product-desp",
                'placeholder': "Enter product description",
                'class': "materialize-textarea",
                'rows': 5,
                'cols': 500
            }
        )
    )
    price = forms.DecimalField(initial=1.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title. Make sure your title contains 'CFE'.")
        else:
            return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        else:
            return title

class RawProductForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : "Enter product name"
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'id': "product-desp",
                'placeholder': "Enter product description",
                'class': "materialize-textarea",
                'rows': 5,
                'cols': 500
            }
        )
    )
    price = forms.DecimalField(initial=1.99)
    featured        = forms.BooleanField()