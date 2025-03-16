from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
                'class':'w-128 h-10 p-2 text-sm text-gray-800 bg-gray-100 rounded-md resize-none'
            }), label='')
    class Meta:
        model=ConversationMessage
        fields =('content',)
        