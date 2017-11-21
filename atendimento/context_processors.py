import datetime

from fluxo.models import Movimentacao
from venda.models import Venda


def pendentes(request):

    vendas_pendentes = Venda.objects.filter(tipo=2, comanda=False, data_pagamento=datetime.date.today(), pago=False)
    context = {
        'vendas_pendentes': vendas_pendentes,
    }
    return context
