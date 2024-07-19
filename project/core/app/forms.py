from django import forms
from apps.site.models import Information

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title', 'content']
