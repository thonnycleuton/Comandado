from django.conf.urls import url

from agendamento.views import *

urlpatterns = [
    url(r'^$', AgendaList.as_view(), name='list'),
]