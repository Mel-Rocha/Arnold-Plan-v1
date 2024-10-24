from django import forms
from .models import DietGeneralInfo

class DietGeneralInfoForm(forms.ModelForm):
    initial_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    final_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = DietGeneralInfo
        fields = ('goal', 'observations', 'initial_date', 'final_date', 'weeks', 'type_of_diet')
        widgets = {
            'type_of_diet': forms.Select(attrs={'class': 'your-css-class'}),
        }

   