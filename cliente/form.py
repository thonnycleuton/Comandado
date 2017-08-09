from django import forms
from django.forms.models import modelformset_factory

from .models import Cliente, Endereco


class ClienteForm(forms.ModelForm):
    # endereco = forms.ModelMultipleChoiceField(
    #     queryset=Endereco.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(attrs={'class': 'icheckbox'})
    # )

    class Meta:
        model = Cliente
        exclude = ('cod_cliente', 'comanda')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control datepicker', }),
            'status_ativo': forms.CheckboxInput(attrs={'class': 'form-control icheckbox'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        exclude = ['cliente', ]
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),

        }


EnderecoFormSet = modelformset_factory(Endereco, EnderecoForm)
