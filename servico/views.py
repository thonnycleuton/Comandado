from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from servico.form import ServicoForm
from .models import Servico


class ServicoList(ListView):
    model = Servico
    ordering = '-cod_servico'
    queryset = Servico.objects.all().order_by('id')
    context_object_name = 'servico_list'


class ServicoCreate(FormView):

    form_class = ServicoForm
    template_name = 'servico/servico_form.html'
    success_url = reverse_lazy('servicos:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ServicoCreate, self).form_valid(form)


class ServicoUpdate(UpdateView):
    model = Servico
    success_url = reverse_lazy('servico_list')
    fields = '__all__'


class ServicoDelete(DeleteView):
    model = Servico
    success_url = reverse_lazy('servico_list')
