from django import forms

from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]
    
    # def clean_title(self):      #Only an on-form validation
    #     title = self.cleaned_data.get('title')
    #     if title.lower() == 'abc':
    #         raise forms.ValidationError("This is not a valid title!")
    #     return title