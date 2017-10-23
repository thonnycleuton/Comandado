from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, CreateView

from fluxo.form import MovimentacaoForm
from fluxo.models import Movimentacao, Tipo


class ListMovimentacao(ListView):
    model = Movimentacao


class CreateMovimentacao(CreateView):
    model = Movimentacao
    form_class = MovimentacaoForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        f = form.save(commit=False)
        f.user = self.request.user
        f.valor = f.valor * (-1) if f.tipo.tipo == 2 else f.valor
        f.save()
        return super(CreateMovimentacao, self).form_valid(form)


class ListMovimentacaoTipo(ListView):
    model = Tipo


class CreateMovimentacaoTipo(CreateView):
    model = Tipo
    fields = '__all__'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(CreateMovimentacaoTipo, self).form_valid(form)
