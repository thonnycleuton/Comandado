from django.shortcuts import render

# Create your views here.
from atendimento.models import Cliente, Servico
from venda.models import Venda


def home(request):
    total_vendas = 0
    vendas = Venda.objects.all()
    for item in vendas:
        total_vendas += item.valor_venda
    context = {'total_vendas': total_vendas}
    print total_vendas
    return render(request, 'index.html', context)


def clientes(request):
    clientes_obj = Cliente.objects.all()
    context = {'clientes': clientes_obj, }
    return render(request, 'clientes.html', context)


def servicos(request):
    servicos_obj = Servico.objects.all()
    context = {'servicos': servicos_obj, }
    return render(request, 'servicos.html', context)


def fornecedores(request):
    return render(request, 'fornecedores.html')


def produtos(request):
    return render(request, 'produtos.html')
