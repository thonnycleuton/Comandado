from django import forms

from fluxo.models import Movimentacao


class MovimentacaoForm(forms.ModelForm):

    class Meta:
        model = Movimentacao
        exclude = {'cod_movimentacao', 'data', 'user', }
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'fonte_destino': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }
