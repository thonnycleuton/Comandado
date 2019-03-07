from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from agendamento.models import Agenda


class AgendaList(ListView):
    model = Agenda
