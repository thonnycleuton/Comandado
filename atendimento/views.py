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

    total_entradas_dinheiro = 0
    total_entradas_cartao = 0
    total_entradas_fiado = 0

    total_saidas_salarios = 0
    total_saidas_socios = 0
    total_saidas_outros = 0

    saidas_mes_atual_valor = 0
    faturamento_semanal = 0
    faturamento_outubro = 0
    faturamento_novembro = 0

    saidas_mes_anterior_valor = 0
    total_entradas = []
    total_saidas = []

    hoje = datetime.date.today()
    dia_primeiro = hoje.replace(day=1)

    servico = Servico.objects.all()
    id_usuario = request.user.id
    perfil = User.objects.get(pk=id_usuario) if id_usuario == 1 else Profile.objects.get(pk=id_usuario)
    # pegando quanitdade de todos os clientes, nao filtrados por data

    # colaboradores = Profile.objects.all()
    colaboradores = Profile.objects.all().exclude(first_name="Thonny").exclude(first_name="Julio")

    clientes = Cliente.objects.all()
    quant_clientes = clientes.count()
    quant_clientes_novos = clientes.filter(created_at__range=(dia_primeiro, hoje)).count()

    gerencia = True if request.user.profile.groups.filter(name='Gerência').exists() else False

    entradas = Movimentacao.objects.filter(tipo__tipo=1)

    ''' Busca o valor de todas as entradas dos ultimos semeses antes do atual
        Busca tambem o mes atual, bem como especificacao do tipo de entrada '''
    for i in range(0, 7):
        total_entradas.append(0)
        # entrada filtrada pelo mes atual (i) e vai regredindo pra iterar sobre os meses anteriores
        entradas_filtro = entradas.filter(data__month=hoje.month - i)
        # itera sobre as vendas filtradas pro mes que se busca (i)
        for entrada in entradas_filtro:
            # calcula o valor total do mes que esta sendo filtrado nesta iteracao do looping
            total_entradas[i] += entrada.valor
            # se a iteracao do loop for 0, ou seja, se o mes do looping for o mes atual, entao busca-se mais informacoes
            if i == 0:
                # calcula o valor total de entradas em dinheiro (4)
                if entrada.tipo.id == 4:
                    total_entradas_dinheiro += entrada.valor
                # calcula o valor total de entradas em cartao de credito ou debito (3)
                elif entrada.tipo.id == 3:
                    total_entradas_cartao += entrada.valor
                # calcula o valor total de entradas de recebimento de fiados (25)
                elif entrada.tipo.id == 27:
                    total_entradas_fiado += entrada.valor

    saidas = Movimentacao.objects.filter(tipo__tipo=2)

    ''' Busca o valor de todas as entradas dos ultimos semeses antes do atual
        Busca tambem o mes atual, bem como especificacao do tipo de entrada '''
    for i in range(0, 7):
        total_saidas.append(0)
        # entrada filtrada pelo mes atual (i) e vai regredindo pra iterar sobre os meses anteriores
        saidas_filtro = saidas.filter(data__month=hoje.month - i)
        # itera sobre as vendas filtradas pro mes que se busca (i)
        for saida in saidas_filtro:
            # calcula o valor total do mes que esta sendo filtrado nesta iteracao do looping
            total_saidas[i] += saida.valor
            # se a iteracao do loop for 0, ou seja, se o mes do looping for o mes atual, entao busca-se mais informacoes
            if i == 0:
                # calcula o valor total de saidas para pagamento de funcionarios (6)
                if saida.tipo.id == 6:
                    total_saidas_salarios += saida.valor
                # calcula o valor total de saida para retirada de socios (7)
                elif saida.tipo.id == 7:
                    total_saidas_socios += saida.valor
                # calcula o valor total de saidas diversas
                else:
                    total_saidas_outros += saida.valor

    for saida in saidas:
        saidas_mes_atual_valor += saida.valor

    saidas_mes_1 = saidas.filter(data__month=hoje.month - 1)

    for saida in saidas_mes_1:
        saidas_mes_anterior_valor += saida.valor

    vendas = Venda.objects.all()

    segunda = datetime.date.today() - datetime.timedelta(datetime.date.today().weekday())

    vendas_semanal = vendas.filter(data_venda__range=(segunda, datetime.date.today() + datetime.timedelta(days=1)))
    for venda in vendas_semanal:
        faturamento_semanal += venda.valor_final

    vendas_outubro = vendas.filter(data_venda__year='2017', data_venda__month='10')
    lista_de_colaboradores = []
    for venda in vendas_outubro:
        faturamento_outubro += venda.valor_final

    vendas_novembro = vendas.filter(data_venda__year='2017', data_venda__month='11', comanda=False)
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
            'faturamento_semanal': faturamento_semanal,
            'meta_outubro': meta_geral,
            'faturamento_outubro': faturamento_outubro,
            'meta_novembro': meta_geral,
            'faturamento_novembro': faturamento_novembro,
        },
        'meta_geral': meta_geral,
        'movimentacao': {
            'entradas': {
                'mes_atual': {
                    'total__dinheiro': total_entradas_dinheiro,
                    'total_dinheiro_porcento': int(total_entradas_dinheiro * 100 / total_entradas[0]),
                    'total_cartao': total_entradas_cartao,
                    'total_cartao_porcento': int(total_entradas_cartao * 100 / total_entradas[0]),
                    'total_fiado': total_entradas_fiado,
                    'total_fiado_porcento': int(total_entradas_fiado * 100 / total_entradas[0]),
                    'total': total_entradas[0],
                },
                'mes_anterior': total_entradas[1],
                'meses_2_atras': total_entradas[2] + 9540,
                'meses_3_atras': total_entradas[3] + 11755,
                'meses_4_atras': total_entradas[4] + 6500,
                'meses_5_atras': total_entradas[5] + 8005,
                'meses_6_atras': total_entradas[6] + 8005,
            },
            'saidas': {
                'mes_atual': {
                    'total_socios': total_saidas_socios * (-1),
                    'total_socios_porcento': int(total_saidas_socios * 100 / total_saidas[0]),
                    'total_salarios': total_saidas_salarios * (-1),
                    'total_salarios_porcento': int(total_saidas_salarios * 100 / total_saidas[0]),
                    'total_outros': total_saidas_outros * (-1),
                    'total_outros_porcento': int(total_saidas_outros * 100 / total_saidas[0]),
                    'total': total_saidas[0] * (-1),
                },
                'mes_anterior': total_saidas[1] * (-1),
                'meses_2_atras': total_saidas[2] + 5540,
                'meses_3_atras': total_saidas[3] + 3755,
                'meses_4_atras': total_saidas[4] + 2500,
                'meses_5_atras': total_saidas[5] + 5005,
                'meses_6_atras': total_saidas[6] + 10005,
            },
        },
        'total_saidas': total_saidas[0] * (-1),
    }
    return render(request, 'index.html', context)
