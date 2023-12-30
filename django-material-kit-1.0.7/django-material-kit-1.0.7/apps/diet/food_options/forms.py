from django import forms
from .models import FoodOptions

class FoodOptionsForm(forms.ModelForm):
    class Meta:
        model = FoodOptions
        fields = ('food', 'quantity', 'unit_of_measurement')
        widgets = {
            'unit_of_measurement': forms.Select(attrs={}),
        }