from datetime import datetime

from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from accounts.models import Profile
from servico.models import Servico
from venda.form import VendaGerenciaForm, VendaSalaoForm, VendaDepilacaoForm, VendaFacialForm, \
    VendaCorporalForm, VendaManicureForm, VendaCaixaForm
from .models import Venda, ItensVenda


class VendaList(ListView):
    model = Venda
    ordering = 'id'
    context_object_name = 'venda_list'

    def get_queryset(self):

        colaborador = Profile.objects.get(pk=self.request.user.pk)

        if colaborador.groups.filter(name__contains='Gerência'):
            vendas = Venda.objects.all()
        elif colaborador.groups.filter(name__contains='Caixa'):
            vendas = Venda.objects.filter(data_venda__day=datetime.today().day)
        else:
            vendas = Venda.objects.filter(data_venda__day=datetime.today().day, comanda=True)

        return vendas


class VendaCreate(FormView):

    template_name = 'venda/venda_form.html'
    success_url = reverse_lazy('vendas:list')

    def get_context_data(self, **kwargs):

        context = super(VendaCreate, self).get_context_data(**kwargs)
        colaborador = Profile.objects.get(pk=self.request.user.pk)

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Salão'):
            context['campo_servicos'] = True
        if colaborador.groups.filter(name__contains='Recepção'):
            context['campo_cliente'] = True
        if colaborador.groups.filter(name__contains='Caixa'):
            context['campo_pagamento'] = True

        return context

    def get_form(self, form_class=None):

        colaborador = Profile.objects.get(pk=self.request.user.pk)

        if colaborador.groups.filter(name__contains='Salão'):
            form_class = VendaSalaoForm
        elif colaborador.groups.filter(name__contains='Estética Facial'):
            form_class = VendaFacialForm
        elif colaborador.groups.filter(name__contains='Estética Corporal'):
            form_class = VendaCorporalForm
        elif colaborador.groups.filter(name__contains='Manicure'):
            form_class = VendaManicureForm
        elif colaborador.groups.filter(name__contains='Depilação'):
            form_class = VendaDepilacaoForm
        elif colaborador.groups.filter(name__contains='Gerência'):
            form_class = VendaGerenciaForm
        else:
            form_class = VendaCaixaForm

        return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        f = form.save(commit=False)
        f.vendedor = self.request.user
        f.save()
        for field in self.request.POST.getlist('servico'):
            for item in self.request.POST.getlist(field):
                ItensVenda.objects.create(cod_venda=f, cod_servico=Servico.objects.get(pk=item))
        return super(VendaCreate, self).form_valid(form)


class VendaUpdate(UpdateView):

    model = Venda
    success_url = reverse_lazy('vendas:list')

    def get_context_data(self, **kwargs):

        context = super(VendaUpdate, self).get_context_data(**kwargs)
        colaborador = Profile.objects.get(pk=self.request.user.pk)

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Salão'):
            context['campo_servicos'] = True
        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Recepção'):
            context['campo_cliente'] = True
        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Caixa'):
            context['campo_pagamento'] = True

        return context

    def get_form(self, form_class=None):

        colaborador = Profile.objects.get(pk=self.request.user.pk)

        if colaborador.groups.filter(name__contains='Salão'):
            form_class = VendaSalaoForm
        elif colaborador.groups.filter(name__contains='Estética Facial'):
            form_class = VendaFacialForm
        elif colaborador.groups.filter(name__contains='Estética Corporal'):
            form_class = VendaCorporalForm
        elif colaborador.groups.filter(name__contains='Manicure'):
            form_class = VendaManicureForm
        elif colaborador.groups.filter(name__contains='Depilação'):
            form_class = VendaDepilacaoForm
        elif colaborador.groups.filter(name__contains='Gerência'):
            form_class = VendaGerenciaForm
        elif colaborador.groups.filter(name__contains='Caixa'):
            form_class = VendaCaixaForm
        elif colaborador.groups.filter(name__contains='Recepção'):
            form_class = VendaCaixaForm

        return form_class(**self.get_form_kwargs())

    def form_valid(self, form):

        f = form.save(commit=False)
        f.vendedor = self.request.user

        if self.request.POST.getlist('tipo'):
            f.comanda = False

        f.save()

        for field in self.request.POST.getlist('servico'):
            item_vendas = ItensVenda(cod_venda=f, cod_servico=Servico.objects.get(pk=field))
            item_vendas.save()

        return HttpResponseRedirect(self.get_success_url())


class VendaDelete(DeleteView):
    model = Venda
    success_url = reverse_lazy('vendas:list')
