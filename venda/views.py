from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from accounts.models import Profile
from servico.models import Servico
from venda.form import VendaGerenciaForm
from .models import Venda, ItensVenda
from estetica import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class VendaList(ListView):
    model = Venda
    ordering = 'id'
    context_object_name = 'venda_list'

    def get_queryset(self):

        data_inicial = self.request.GET.get('data_inicial')
        data_final = self.request.GET.get('data_final')

        if self.request.user.groups.filter(name__contains='Gerência'):
            if data_final or data_inicial:
                date = datetime.strptime(data_final, '%Y-%m-%d')
                date += timedelta(days=1)
                vendas = Venda.objects.filter(data_venda__range=(data_inicial, date))
            else:
                vendas = Venda.objects.all()

        elif self.request.user.groups.filter(name__contains='Caixa'):
            vendas = Venda.objects.filter(data_venda__day=datetime.today().day)
        else:
            vendas = Venda.objects.filter(data_venda__day=datetime.today().day, comanda=True)

        return vendas


@method_decorator(login_required, name='dispatch')
class VendaCreate(FormView):
    template_name = 'venda/venda_form.html'
    success_url = reverse_lazy('vendas:list')

    def get_form_kwargs(self):
        kwargs = super(VendaCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):

        context = super(VendaCreate, self).get_context_data(**kwargs)
        colaborador = Profile.objects.get(pk=self.request.user.pk)

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Salão'):
            context['campo_servicos'] = True
        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Recepção'):
            context['campo_cliente'] = True
        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Caixa'):
            context['campo_pagamento'] = True
        if colaborador.groups.filter(name__contains='Gerência'):
            context['campo_comanda'] = True

        return context

    def get_form(self, form_class=None):

        form_class = VendaGerenciaForm

        return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        f = form.save(commit=False)
        f.vendedor = self.request.user
        f.save()
        for item in self.request.POST.getlist('servico'):
            ItensVenda.objects.create(cod_venda=f, cod_servico=Servico.objects.get(pk=item))
        return super(VendaCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class VendaUpdate(UpdateView):
    model = Venda
    success_url = reverse_lazy('vendas:list')

    def get_form_kwargs(self):
        kwargs = super(VendaUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):

        context = super(VendaUpdate, self).get_context_data(**kwargs)
        colaborador = Profile.objects.get(pk=self.request.user.pk)

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Salão'):
            context['campo_servicos'] = True

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(
                name__contains='Estética Facial'):
            context['campo_servicos'] = True

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(
                name__contains='Estética Corporal'):
            context['campo_servicos'] = True

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Manicure'):
            context['campo_servicos'] = True

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(
                name__contains='Depilação'):
            context['campo_servicos'] = True

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Recepção'):
            context['campo_cliente'] = True

        if colaborador.groups.filter(name__contains='Gerência') or colaborador.groups.filter(name__contains='Caixa'):
            context['campo_pagamento'] = True

        if colaborador.groups.filter(name__contains='Gerência'):
            context['campo_comanda'] = True

        return context

    def get_form(self, form_class=None):

        form_class = VendaGerenciaForm

        return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        # intancia um objeto do tipo profile que eh uma heranca de USER
        colaborador = self.request.user

        f = form.save(commit=False)
        f.vendedor = self.request.user
        # checa se o campo comanda nao foi alterado por um colaborador da Gerencia ou do Caixa para fechar a Comanda
        if not 'comanda' in form.changed_data and colaborador.profile.groups.filter(
                name__contains='Gerência') or colaborador.profile.groups.filter(name__contains='Caixa'):
            f.comanda = False

        f.save()

        remover = set(form.initial['servico']).difference(form.cleaned_data['servico'])

        if remover and colaborador.profile.groups.filter(name__contains='Gerência'):
            for item in remover:
                ItensVenda.objects.get(cod_servico=item.pk, cod_venda=f).delete()

        for field in self.request.POST.getlist('servico'):
            # checa se o item de servico ja existe para inserir um novo item de servico à venda
            if not ItensVenda.objects.filter(cod_venda=f, cod_servico=Servico.objects.get(pk=field)).exists():
                item_vendas = ItensVenda(cod_venda=f, cod_servico=Servico.objects.get(pk=field))
                item_vendas.save()

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class VendaDelete(DeleteView):
    model = Venda
    success_url = reverse_lazy('vendas:list')
