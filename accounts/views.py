import json

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.urls import reverse_lazy

from accounts.models import Profile
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from haystack.query import SearchQuerySet


def alterar_privilegio(request, pk):

    p = Profile.objects.get(pk=pk)
    p.is_superuser = not p.is_superuser
    p.save()
    return redirect("/contas/usuarios/")


def alterar_status(request, pk):

    p = Profile.objects.get(pk=pk)
    p.is_active = not p.is_active
    p.save()
    return redirect("/contas/usuarios/")


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.username for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')


class ListPerfil(ListView):
    model = Profile
    context_object_name = 'perfil_list'

    def get_queryset(self):
        queryset = super(ListPerfil, self).get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset


class ListPerfis(ListView):
    model = Profile
    template_name = 'accounts/usuarios.html'
    context_object_name = 'perfil_list'


class CreatePerfil(CreateView):
    model = Profile
    fields = {'password', 'first_name', 'foto', 'email', 'is_superuser', 'is_active'}
    success_url = reverse_lazy('contas:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(CreatePerfil, self).form_valid(form)


class PerfilDelete(DeleteView):
    model = Profile
    success_url = "/contas/usuarios/"
