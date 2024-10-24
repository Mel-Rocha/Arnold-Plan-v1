from django import forms

from apps.diet.food_options.models import FoodOptions


class FoodOptionsForm(forms.ModelForm):
    class Meta:
        model = FoodOptions
        fields = ('food', 'quantity', 'unit_of_measurement')
        widgets = {
            'unit_of_measurement': forms.Select(attrs={}),
        }
