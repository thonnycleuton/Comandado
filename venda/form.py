from django import forms

from servico.models import Servico
from venda.models import Venda, ItensVenda


class VendaGerenciaForm(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['cod_cliente', 'servico', 'tipo', 'comanda']
        widgets = {
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control select'}),
            'comanda': forms.CheckboxInput(attrs={'class': 'icheckbox'}),
        }


class VendaDepilacaoForm(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=1),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['servico', ]


class VendaFacialForm(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=2),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['servico', ]


class VendaCorporalForm(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=3),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['servico', ]


class VendaManicureForm(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=4),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['servico', ]


class VendaSalaoForm(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=5),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['servico', ]


class VendaRecepcaoForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cod_cliente', ]


class VendaCaixaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['tipo', 'comanda']


class VendaForm2(forms.ModelForm):
    servico = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=1),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    servico2 = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=2),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    servico3 = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=3),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    servico4 = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=4),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    servico5 = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Servico.objects.filter(categoria=5),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    )

    class Meta:
        model = Venda
        fields = ['cod_cliente', 'servico', 'tipo', 'comanda']
        widgets = {
            'cod_cliente': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(attrs={'class': 'iradio'}),
            'comanda': forms.CheckboxInput(attrs={'class': 'icheckbox'}),
        }
