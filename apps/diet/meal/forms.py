from django import forms

from apps.diet.meal.models import Meal
from apps.diet.meal_general_info.models import MealGeneralInfo


class MealGeneralInfoInlineForm(forms.ModelForm):
    class Meta:
        model = MealGeneralInfo
        fields = ('name', 'time', 'type_of_meal')
        widgets = {
            'type_of_meal': forms.Select(attrs={}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class MealForm(forms.ModelForm):
    meal_general_info = MealGeneralInfoInlineForm()

    class Meta:
        model = Meal
        fields = ('diet',)
