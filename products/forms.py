from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
    title           = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : "Enter product name"
            }
        )
    )
    price           = forms.DecimalField(initial=1.99)
    class Meta:
        model = Product
        fields = [
            "title", "description", "price"
        ]
    
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     else:
    #         return title


class RawProductForm(forms.Form):
    title           = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : "Enter product name"
            }
        )
    )
    description     = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Enter a description",
                'class' : "materialize-textarea",
                'id' : "id",
                'rows' : 50
            }
        )
    )
    price           = forms.DecimalField(initial=1.99)
    featured        = forms.BooleanField()