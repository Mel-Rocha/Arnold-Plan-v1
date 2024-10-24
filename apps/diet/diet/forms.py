from django import forms

from apps.diet.diet.models import Diet
from apps.diet.diet_general_info.models import DietGeneralInfo


class DietGeneralInfoInlineForm(forms.ModelForm):
    initial_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    final_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DietGeneralInfo
        fields = ('goal', 'observations', 'initial_date', 'final_date', 'weeks', 'type_of_diet')


class DietForm(forms.ModelForm):
    diet_general_info = DietGeneralInfoInlineForm()

    class Meta:
        model = Diet
        fields = ('profile',)
