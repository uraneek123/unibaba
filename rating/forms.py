from django import forms
from .models import Rating

class RatingMessageForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields =('description',)
        widgets={
            'description': forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
            
        }