from django import forms

from servico.models import Servico
from venda.models import Venda, ItensVenda


class VendaGerenciaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user')
        super(VendaGerenciaForm, self).__init__(*args, **kwargs)

        if self.user.groups.filter(name="Gerência"):
            servicos = Servico.objects.all()
        else:
            servicos = Servico.objects.filter(categoria__in=self.user.groups.all())
            del self.fields['comanda']

            if not self.user.groups.filter(name="Recepção"):
                del self.fields['cod_cliente']
            if not self.user.groups.filter(name="Caixa"):
                del self.fields['tipo']

        self.fields['servico'].queryset = servicos

    class Meta:

        model = Venda
        fields = ['cod_cliente', 'servico', 'tipo', 'comanda', 'desconto', 'data_pagamento']
        widgets = {
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(),
            'comanda': forms.CheckboxInput(attrs={'class': 'switch-radio1'}),
            'servico': forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'}),
            'desconto': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_pagamento': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        }


class ItensFormView(forms.ModelForm):

    desconto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ItensVenda
        fields = ['desconto']
