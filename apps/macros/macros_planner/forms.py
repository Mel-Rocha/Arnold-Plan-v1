from django import forms

from apps.macros.macros_planner.models import MacrosPlanner
from apps.macros.general_info.models import GeneralInfo


class GeneralInfoInlineForm(forms.ModelForm):
    initial_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    final_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = GeneralInfo
        fields = ('goal', 'initial_date', 'final_date', 'weeks')


class MacrosPlannerForm(forms.ModelForm):
    general_info = GeneralInfoInlineForm()

    class Meta:
        model = MacrosPlanner
        fields = ('profile',)
