
from django.core.management.base import BaseCommand

from fluxo.models import Movimentacao
from venda.models import Venda

__author__ = 'Thonny Cleuton'


class Command(BaseCommand):

    help = "Inserir movimentacao de cartoes que antes nao eram contadas como entradas"

    vendas = Venda.objects.all().exclude(tipo=1).exclude(tipo=2)

    for venda in vendas:

        movimentcao = Movimentacao.objects.create(valor=venda.valor_final, user_id=1, tipo_id=3, fonte_destino=venda.cod_venda)
        movimentcao.data = venda.data_venda
        movimentcao.save()

