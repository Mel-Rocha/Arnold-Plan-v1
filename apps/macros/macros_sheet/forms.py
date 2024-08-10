from django import forms
from .models import MacrosSheet


class MacrosSheetForm(forms.ModelForm):
    class Meta:
        model = MacrosSheet
        fields = ['cho', 'ptn', 'fat']

    def clean(self):
        cleaned_data = super().clean()
        cho = cleaned_data.get('cho')
        ptn = cleaned_data.get('ptn')
        fat = cleaned_data.get('fat')

        return cleaned_data
