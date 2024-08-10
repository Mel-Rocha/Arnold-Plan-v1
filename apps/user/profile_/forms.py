from django import forms

from apps.user.profile_.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'birth_date', 'weight', 'height', 'gender')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),

        }
