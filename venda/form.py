from django import forms

from venda.models import Venda


class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ['cod_venda', 'cod_servico', 'cod_cliente', 'tipo', 'vendedor']
        widgets = {
            'cod_venda': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_servico': forms.Select(attrs={'class': 'form-control'}),
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(attrs={'class': 'form-control check iradio'})
        }
