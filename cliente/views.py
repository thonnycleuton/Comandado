from django.db import transaction
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from cliente.form import ClienteForm, EnderecoFormSet
from .models import Cliente


class ServerList(ListView):
    model = Cliente
    ordering = '-cod_cliente'
    queryset = Cliente.objects.all()
    context_object_name = 'cliente_list'


class ServerCreate(CreateView):
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('clientes:list')

    def get_context_data(self, **kwargs):
        data = super(ServerCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['enderecos'] = EnderecoFormSet(self.request.POST)
        else:
            data['enderecos'] = EnderecoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        enderecos = context['enderecos']
        with transaction.atomic():
            self.object = form.save()
            if enderecos.is_valid():
                enderecos.instance = self.object
                enderecos.save()
        form.save()
        return super(ServerCreate, self).form_valid(form)


class ServerUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')


class ServerDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('server_list')
