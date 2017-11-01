import datetime

from django.contrib.auth.models import User

from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from estetica import settings
from fluxo.models import Movimentacao
from servico.models import Servico
from cliente.models import Cliente
from venda.models import Venda


@login_required(login_url=settings.LOGIN_URL)
def home(request):
    faturamento = 0
    meta_geral = 0
    total_entradas = 0
    total_entradas_dinheiro = 0
    total_entradas_cartao = 0
    total_entradas_fiado = 0
    total_saidas = 0
    faturamento_outubro = 0
    faturamento_novembro = 0


    hoje = datetime.date.today()
    dia_primeiro = hoje.replace(day=1)

    servico = Servico.objects.all()
    id_usuario = request.user.id
    perfil = User.objects.get(pk=id_usuario) if id_usuario == 1 else Profile.objects.get(pk=id_usuario)
    # pegando quanitdade de todos os clientes, nao filtrados por data

    clientes = Cliente.objects.all()
    # colaboradores = Profile.objects.all()
    colaboradores = Profile.objects.all().exclude(first_name="Thonny").exclude(first_name="Julio")
    quant_clientes = clientes.count()
    quant_clientes_novos = clientes.filter(created_at__range=(dia_primeiro, hoje)).count()
    gerencia = True if request.user.profile.groups.filter(name='Gerência').exists() else False

    entradas = Movimentacao.objects.filter(tipo__tipo=1).filter(data__year=hoje.year, data__month=hoje.month)

    for entrada in entradas:

        total_entradas += entrada.valor

        if entrada.tipo.id == 4:
            total_entradas_dinheiro += entrada.valor
        elif entrada.tipo.id == 3:
            total_entradas_cartao += entrada.valor
        elif entrada.tipo.id == 25:
            total_entradas_fiado += entrada.valor

    saidas = Movimentacao.objects.filter(tipo__tipo=2).filter(data__year=hoje.year, data__month=hoje.month)
    for saida in saidas:
        total_saidas += saida.valor
    vendas = Venda.objects.all()

    vendas_outubro = vendas.filter(data_venda__year='2017', data_venda__month='10')
    for venda in vendas_outubro:
        faturamento_outubro += venda.valor_final

    vendas_novembro = vendas.filter(data_venda__year='2017', data_venda__month='11')
    for venda in vendas_novembro:
        faturamento_novembro += venda.valor_final


    for s in servico:
        faturamento += s.get_faturamento()

    for colaborador in colaboradores:
        meta_geral += colaborador.meta

    context = {
        'gerencia': gerencia,
        'servicos': servico,
        'colaboradores': colaboradores,
        'faturamento': faturamento,
        'data_atual': hoje,
        'quant_clientes': quant_clientes,
        'quant_clientes_novos': quant_clientes_novos,
        'perfil': perfil,
        'metas_realizacoes': {
            'meta_outubro': meta_geral,
            'faturamento_outubro': faturamento_outubro,
            'meta_novembro': meta_geral,
            'faturamento_novembro': faturamento_novembro,
        },
        'meta_geral': meta_geral,
        'entradas': {
            'total_dinheiro': total_entradas_dinheiro,
            'total_dinheiro_porcento': int(total_entradas_dinheiro * 100/total_entradas),
            'total_cartao': total_entradas_cartao,
            'total_cartao_porcento': int(total_entradas_cartao * 100/total_entradas),
            'total_fiado': total_entradas_fiado,
            'total_fiado_porcento': int(total_entradas_fiado * 100/total_entradas),
            'total': total_entradas,
        },
        'total_saidas': total_saidas * (-1),
    }
    return render(request, 'index.html', context)
