from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from cliente.form import ClienteForm, EnderecoFormSet
from .models import Cliente, Endereco


class ServerList(ListView):
    model = Cliente
    ordering = '-cod_cliente'
    queryset = Cliente.objects.all()
    context_object_name = 'cliente_list'


class ServerCreate(CreateView):
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('clientes:list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def form_valid(self, form):
        # override the ModelFormMixin definition so you don't save twice
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = EnderecoFormSet(queryset=Endereco.objects.none())
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = EnderecoFormSet(request.POST)
        form_valid = form.is_valid()
        formset_valid = formset.is_valid()
        if form_valid and formset_valid:
            self.object = form.save()
            enderecos = formset.save(commit=False)
            for endereco in enderecos:
                endereco.cliente = self.object
                endereco.save()
            formset.save_m2m()
            return self.form_valid(form)
        else:
            return self.form_invalid(form, formset)


class ServerUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def form_valid(self, form):
        # override the ModelFormMixin definition so you don't save twice
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = EnderecoFormSet(queryset=Endereco.objects.filter(cliente=self.object))
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = EnderecoFormSet(request.POST)
        form_valid = form.is_valid()
        formset_valid = formset.is_valid()
        if form_valid and formset_valid:
            self.object = form.save()
            enderecos = formset.save(commit=False)
            for endereco in enderecos:
                endereco.cliente = self.object
                endereco.save()
            formset.save_m2m()
            return self.form_valid(form)
        else:
            return self.form_invalid(form, formset)


class ServerDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('server_list')


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    data = dict()
    if request.method == 'POST':
        cliente.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        clientes = Cliente.objects.all()
        data['html_list'] = render_to_string('cliente/includes/partial_cliente_list.html',
                                                     {'cliente_list': clientes})
    else:
        context = {'cliente': cliente}
        data['html_form'] = render_to_string('cliente/includes/partial_cliente_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)
