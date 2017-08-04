from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'is_superuser', 'is_active', 'telefone', 'funcao', 'foto']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control icheckbox'}),
            'funcao': forms.TextInput(attrs={'class': 'form-control icheckbox'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-control icheckbox'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control icheckbox'}),
            'foto': forms.FileInput(attrs={'class': 'btn-primary'}),
        }