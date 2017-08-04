from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from servico.models import Servico
from venda.form import VendaForm
from .models import Venda, ItensVenda


class VendaList(ListView):
    model = Venda
    ordering = 'id'
    queryset = Venda.objects.all()
    context_object_name = 'venda_list'


class VendaCreate(FormView):
    form_class = VendaForm
    template_name = 'venda/venda_form.html'
    success_url = reverse_lazy('vendas:list')

    def form_valid(self, form):
        f = form.save(commit=False)
        f.vendedor = self.request.user
        f.save()
        for item in self.request.POST.getlist('servico'):
            ItensVenda.objects.create(cod_venda=f, cod_servico=Servico.objects.get(pk=item))
        return super(VendaCreate, self).form_valid(form)


class VendaUpdate(UpdateView):
    model = Venda
    success_url = reverse_lazy('vendas:list')
    fields = ['servico', 'cod_cliente', 'tipo', 'valor_venda']

    def form_valid(self, form):
        f = form.save(commit=False)
        f.save()
        for item in self.request.POST.getlist('servico'):
            item_vendas = ItensVenda(cod_venda=f, cod_servico=Servico.objects.get(pk=item))
            item_vendas.save()
        return HttpResponseRedirect(self.get_success_url())


class VendaDelete(DeleteView):
    model = Venda
    success_url = reverse_lazy('vendas:list')
