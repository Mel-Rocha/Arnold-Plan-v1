from django import forms
from .models import MealGeneralInfo

class MealGeneralInfoForm(forms.ModelForm):
    class Meta:
        model = MealGeneralInfo
        fields = ('name', 'time', 'type_of_meal')
        widgets = {
            'type_of_meal': forms.Select(attrs={}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    