from django import forms

from servico.models import Servico
from venda.models import Venda, ItensVenda


class VendaForm(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        queryset=Servico.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['cod_venda', 'servico', 'cod_cliente', 'tipo', 'vendedor']
        widgets = {
            'cod_venda': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(attrs={'class': 'iradio'}),
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
        }
