from django import forms
from .models import Servico


class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'cod_servico': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'status_ativo': forms.CheckboxInput(attrs={'class': 'icheckbox'})
        }
