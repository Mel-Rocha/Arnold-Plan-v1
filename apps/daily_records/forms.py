from django import forms

from apps.daily_records.models import DailyRecords

class DailyRecordsForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DailyRecords
        fields = ['date', 'morning_meal', 'afternoon_meal', 'evening_meal', 'bowel_movements', 'hunger_times', 'stress_times',
                  'anxiety_times', 'craving_times']
        widgets = {
            'hunger_times': forms.Select(choices=DailyRecords.TIME_CHOICES),
            'stress_times': forms.Select(choices=DailyRecords.TIME_CHOICES),
            'anxiety_times': forms.Select(choices=DailyRecords.TIME_CHOICES),
            'craving_times': forms.Select(choices=DailyRecords.TIME_CHOICES),
        }