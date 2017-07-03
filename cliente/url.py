from django.conf.urls import url
from cliente.views import ServerList, ServerCreate, ServerUpdate, ServerDelete

urlpatterns = [
    url(r'^$', ServerList.as_view(), name='list'),
    url(r'^novo/$', ServerCreate.as_view(), name='novo'),
    url(r'^editar/(?P<pk>\d+)/$', ServerUpdate.as_view(), name='edite'),
    url(r'^delete/(?P<pk>\d+)/$', ServerDelete.as_view(), name='delete'),
]