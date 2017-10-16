from datetime import datetime

from django.contrib.auth.models import User

from accounts.models import Profile
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from estetica import settings
from servico.models import Servico
from cliente.models import Cliente


@login_required(login_url=settings.LOGIN_URL)
def home(request):
    faturamento = 0

    servico = Servico.objects.all()
    id_usuario = request.user.id
    perfil = User.objects.get(pk=id_usuario) if id_usuario == 1 else Profile.objects.get(pk=id_usuario)
    # pegando quanitdade de todos os clientes, nao filtrados por data

    clientes = Cliente.objects.all()
    colaboradores = Profile.objects.all()
    quant_clientes = clientes.count()
    quant_clientes_novos = clientes.filter()
    gerencia = True if request.user.profile.groups.filter(name='Gerência').exists() else False
    for s in servico:
        faturamento += s.get_faturamento()
    context = {
        'gerencia': gerencia,
        'servicos': servico,
        'colaboradores': colaboradores,
        'faturamento': faturamento,
        'data_atual': datetime.now(),
        'quant_clientes': quant_clientes,
        'perfil': perfil,
    }
    return render(request, 'index.html', context)