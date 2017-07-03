from django.shortcuts import render

# Create your views here.
from atendimento.models import Cliente, Servico


def home(request):
    return render(request, 'index.html')


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
