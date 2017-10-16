from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'telefone', 'funcao', 'foto', 'groups', 'meta']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control'}),

            'telefone': forms.TextInput(attrs={'class': 'phone form-control'}),
            'funcao': forms.Select(attrs={'class': 'form-control'}),
            'meta': forms.NumberInput(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control icheckbox'}),
            'foto': forms.FileInput(attrs={'class': 'btn-primary'}),
        }
