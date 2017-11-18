from datetime import datetime, timedelta

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from fluxo.form import MovimentacaoForm
from fluxo.models import Movimentacao, Tipo
from venda.models import Venda


class ListReceber(ListView):
    model = Venda


class ListMovimentacao(ListView):
    model = Movimentacao

    def get_queryset(self):

        data_inicial = self.request.GET.get('data_inicial')
        data_final = self.request.GET.get('data_final')

        if data_final or data_inicial:
            date = datetime.strptime(data_final, '%Y-%m-%d')
            date += timedelta(days=1)
            movimentacoes = Movimentacao.objects.filter(data__range=(data_inicial, date))
        else:
            movimentacoes = Movimentacao.objects.filter(data__year=datetime.today().year,
                                                        data__month=datetime.today().month)

        return movimentacoes


class CreateMovimentacao(CreateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    success_url = reverse_lazy('movimentacao:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        f = form.save(commit=False)
        f.user = self.request.user
        f.valor = f.valor * (-1) if f.tipo.tipo == 2 else f.valor
        f.save()
        return super(CreateMovimentacao, self).form_valid(form)


class UpdateMovimentacao(UpdateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    success_url = reverse_lazy('movimentacao:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        f = form.save(commit=False)
        f.user = self.request.user
        f.valor = f.valor * (-1) if f.tipo.tipo == 2 else f.valor
        f.save()
        return super(UpdateMovimentacao, self).form_valid(form)


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


def create_prazo(request, cod_venda):

    venda = Venda.objects.get(cod_venda=cod_venda)
    Movimentacao.objects.create(valor=venda.valor_final, user=request.user, tipo_id=27, fonte_destino=venda.cod_cliente.nome, link=venda.get_absolute_url())
    return reverse_lazy('movimentacao:list')
