from django import forms
from .models import Profile, Gender

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'birth_date', 'weight', 'height', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }
       
      
