from datetime import datetime

from django.contrib.auth.models import User

from accounts.models import Profile
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from estetica import settings
from fluxo.models import Movimentacao
from servico.models import Servico
from cliente.models import Cliente


@login_required(login_url=settings.LOGIN_URL)
def home(request):

    faturamento = 0
    meta_geral = 0
    total_entradas = 0
    total_saidas = 0

    servico = Servico.objects.all()
    id_usuario = request.user.id
    perfil = User.objects.get(pk=id_usuario) if id_usuario == 1 else Profile.objects.get(pk=id_usuario)
    # pegando quanitdade de todos os clientes, nao filtrados por data

    clientes = Cliente.objects.all()
    colaboradores = Profile.objects.all()
    # colaboradores = Profile.objects.exclude(groups__name__contains='Gerência')
    quant_clientes = clientes.count()
    quant_clientes_novos = clientes.filter()
    gerencia = True if request.user.profile.groups.filter(name='Gerência').exists() else False
    entradas = Movimentacao.objects.filter(tipo__tipo=1)
    for entrada in entradas:
        total_entradas += entrada.valor
    saidas = Movimentacao.objects.filter(tipo__tipo=2)
    for saida in saidas:
        total_saidas += saida.valor

    for s in servico:
        faturamento += s.get_faturamento()

    for colaborador in colaboradores:
        meta_geral += colaborador.meta

    context = {
        'gerencia': gerencia,
        'servicos': servico,
        'colaboradores': colaboradores,
        'faturamento': faturamento,
        'data_atual': datetime.now(),
        'quant_clientes': quant_clientes,
        'perfil': perfil,
        'meta_geral': meta_geral,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas * (-1),
    }
    return render(request, 'index.html', context)