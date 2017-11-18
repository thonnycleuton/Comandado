
from django.conf.urls import url

from fluxo.views import ListMovimentacao, CreateMovimentacao, ListMovimentacaoTipo, CreateMovimentacaoTipo, \
    UpdateMovimentacao, create_prazo

urlpatterns = [
    url(r'^$', ListMovimentacao.as_view(), name='list'),
    url(r'^novo/$', CreateMovimentacao.as_view(), name='novo'),
    url(r'^novo_prazo/(?P<cod_venda>\w+)/$', create_prazo, name='novo_prazo'),
    url(r'^editar/(?P<pk>\d+)/$', UpdateMovimentacao.as_view(), name='edite'),
    url(r'^tipo/$', ListMovimentacaoTipo.as_view(), name='tipo_list'),
    url(r'^tipo_novo/$', CreateMovimentacaoTipo.as_view(), name='tipo_novo'),
]