from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from fluxo.models import Movimentacao, Tipo


class ListMovimentacao(ListView):
    model = Movimentacao


class CreateMovimentacao(CreateView):
    model = Movimentacao
    fields = '__all__'


class ListMovimentacaoTipo(ListView):
    model = Tipo


class CreateMovimentacaoTipo(CreateView):
    model = Tipo
    fields = '__all__'
