from django.conf.urls import url
from venda.views import VendaList, VendaCreate, VendaUpdate, VendaDelete

urlpatterns = [
    url(r'^$', VendaList.as_view(), name='list'),
    url(r'^novo/$', VendaCreate.as_view(), name='novo'),
    url(r'^editar/(?P<pk>\d+)/$', VendaUpdate.as_view(), name='edite'),
    url(r'^delete/$', VendaDelete.as_view(), name='delete'),
]