from django import forms
from .models import Profile, Gender

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=[(gender.value, gender.name) for gender in Gender],
                               widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['name', 'birth_date', 'weight', 'height', 'gender']
