from django import forms

from servico.models import Servico
from venda.models import Venda, ItensVenda


class VendaAtendimentoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VendaAtendimentoForm, self).__init__(*args, **kwargs)
        self.fields['servico'].queryset.filter(categoria=1)

    class Meta:
        model = Venda
        fields = ['servico', ]


class VendaForm2(forms.ModelForm):

    servico = forms.ModelMultipleChoiceField(
        queryset=Servico.objects.filter(categoria=1),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['cod_cliente', 'servico', 'tipo', ]
        widgets = {
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(attrs={'class': 'iradio'}),
        }
