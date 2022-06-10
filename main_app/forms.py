
from django import forms
from .models import Client, Interview


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('status', 'name', 'position', 'image', 'email',
                  'phone', 'resume', 'linkedin', 'notes')
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),

        }


# class InterviewForm(forms.ModelForm):
    # class Meta:
    #     model = Interview
    #     fields = ('title', 'company', 'date', 'feedback', 'result', 'notes')
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-control'}),
    #         'company': forms.TextInput(attrs={'class': 'form-control'}),
    #         'date': forms.DateField(attrs={'class': 'form-control'}),
    #         'feedback': forms.TextInput(attrs={'class': 'form-control'}),
    #         'result': forms.TextInput(attrs={'class': 'form-control'}),
    #         'notes': forms.TextArea(attrs={'class': 'form-control'}),
    #     }
