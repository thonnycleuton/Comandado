from django import forms
from .models import Servico


class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'valor', 'status_ativo', 'foto', ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'status_ativo': forms.CheckboxInput(attrs={'class': 'icheckbox'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
