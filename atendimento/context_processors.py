import datetime

from cliente.models import Cliente
from fluxo.models import Movimentacao
from venda.models import Venda


def pendentes(request):

    vendas_pendentes = Venda.objects.filter(tipo=2, comanda=False, data_pagamento=datetime.date.today(), pago=False)
    aniversariantes = Cliente.objects.filter(nascimento__day=datetime.date.today().day, nascimento__month=datetime.date.today().month)

    context = {
        'alertas':{
            'tamanho': len(aniversariantes) + len(vendas_pendentes),
            'aniversariantes': aniversariantes,
            'vendas_pendentes': vendas_pendentes,
        },
    }
    return context
