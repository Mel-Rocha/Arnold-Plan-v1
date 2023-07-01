from django import forms
from .models import Profile, Gender

class ProfileForm(forms.ModelForm):
    GENDER_CHOICES = [(gender.value, gender.name) for gender in Gender]

    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = Profile
        fields = ['name', 'birth_date', 'weight', 'height', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['class'] = 'form-select'
