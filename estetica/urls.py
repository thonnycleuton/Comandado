"""estetica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from accounts.views import autocomplete
from django.conf.urls import url, include
from django.contrib import admin

from atendimento.views import home, clientes, fornecedores, produtos, servicos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls', namespace='search')),
    url(r'^autocomplete/', autocomplete, name='autocomplete'),
    url(r'^clientes/', include('cliente.url', namespace='clientes')),
    url(r'^servicos/', include('servico.url', namespace='servicos')),
    url(r'^vendas/', include('venda.url', namespace='vendas')),
    # item de vendas
    url(r'^detalhes/', include('venda.url', namespace='detalhes')),
    url(r'^contas/', include('accounts.url', namespace='contas')),
    url(r'^agenda/', include('agendamento.url', namespace='agenda')),
    url(r'^fornecedores/', fornecedores, name='fornecedores'),
    url(r'^produtos/', produtos, name='produtos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)