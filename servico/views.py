from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from servico.form import ServicoForm
from .models import Servico


class ServicoList(ListView):
    model = Servico
    ordering = '-cod_servico'
    queryset = Servico.objects.all()


class ServicoCreate(CreateView):

    model = Servico
    form_class = ServicoForm
    success_url = reverse_lazy('servicos:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ServicoCreate, self).form_valid(form)


class ServicoUpdate(UpdateView):
    model = Servico
    form_class = ServicoForm
    success_url = reverse_lazy('servicos:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ServicoUpdate, self).form_valid(form)


class ServicoDelete(DeleteView):
    model = Servico
    success_url = reverse_lazy('servico_list')
