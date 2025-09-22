from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm
from .models import Profile

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Removed 'first_name', 'last_name'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'border rounded px-2 py-1 w-full'}),
        }

class PasswordChangeForm(DjangoPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'border rounded px-2 py-1 w-full'})