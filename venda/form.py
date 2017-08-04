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
        fields = ['cod_cliente', 'servico', 'tipo', ]
        widgets = {
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(attrs={'class': 'iradio'}),
        }
