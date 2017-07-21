from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from cliente.form import ClienteForm
from .models import Cliente


class ServerList(ListView):
    model = Cliente
    ordering = '-cod_cliente'
    queryset = Cliente.objects.all()
    context_object_name = 'cliente_list'


class ServerCreate(FormView):
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('clientes:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ServerCreate, self).form_valid(form)


class ServerUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')


class ServerDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('server_list')
