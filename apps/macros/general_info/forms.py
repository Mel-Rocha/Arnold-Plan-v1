from django import forms
from .models import GeneralInfo


class GeneralInfoForm(forms.ModelForm):
    initial_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    final_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = GeneralInfo
        fields = ('goal', 'initial_date', 'final_date', 'weeks')
