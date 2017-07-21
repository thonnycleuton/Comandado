from django.conf.urls import url
from servico.views import ServicoList, ServicoCreate, ServicoUpdate, ServicoDelete

urlpatterns = [
    url(r'^$', ServicoList.as_view(), name='list'),
    url(r'^novo/$', ServicoCreate.as_view(), name='novo'),
    url(r'^edite/(?P<pk>\d+)/$', ServicoUpdate.as_view(), name='edite'),
    url(r'^delete/(?P<pk>\d+)/$', ServicoDelete.as_view(), name='delete'),
]