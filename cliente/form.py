from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'estado_civil', 'sexo', 'nascimento', 'status_ativo', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control datepicker',}),
            'status_ativo': forms.CheckboxInput(attrs={'class': 'form-control icheckbox'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
