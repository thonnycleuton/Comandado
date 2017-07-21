from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from estetica import settings
from servico.models import Servico
from cliente.models import Cliente


@login_required(login_url=settings.LOGIN_URL)
def home(request):
    faturamento = 0

    servico = Servico.objects.all()
    # pegando quanitdade de todos os clientes, nao filtrados por data
    quant_clientes = Cliente.objects.all().count()
    for s in servico:
        faturamento += s.get_faturamento()
    context = {
        'servicos': servico,
        'faturamento': faturamento,
        'data_atual': datetime.now(),
        'quant_clientes': quant_clientes,
    }
    return render(request, 'index.html', context)


def clientes(request):
    clientes_obj = Cliente.objects.all()
    context = {'clientes': clientes_obj,}
    return render(request, 'clientes.html', context)


def servicos(request):
    servicos_obj = Servico.objects.all()
    context = {'servicos': servicos_obj,}
    return render(request, 'servicos.html', context)


def fornecedores(request):
    return render(request, 'fornecedores.html')


def produtos(request):
    return render(request, 'produtos.html')
