from django import forms

from servico.models import Servico
from venda.models import Venda


class VendaForm(forms.ModelForm):

    itens_venda = forms.ModelMultipleChoiceField(
        queryset=Servico.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['cod_venda', 'itens_venda', 'cod_cliente', 'tipo', 'vendedor']
        widgets = {
            'cod_venda': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(attrs={'class': 'iradio'}),
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
        }
