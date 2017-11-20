import datetime

from fluxo.models import Movimentacao
from venda.models import Venda


def pendentes(request):

    pagos = Movimentacao.objects.filter(tipo_id=27)
    vendas_pendentes = Venda.objects.filter(tipo=2, data_pagamento=datetime.date.today())
    for movimento in pagos:
        vendas_pendentes = vendas_pendentes.exclude(cod_cliente__nome=movimento.fonte_destino)
    context = {
        'vendas_pendentes': vendas_pendentes,
    }
    return context
