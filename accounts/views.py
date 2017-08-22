import json

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from accounts.form import ProfileForm
from accounts.models import Profile
from django.shortcuts import render, redirect, get_object_or_404

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
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:3]
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
    template_name = 'accounts/profile_list.html'

    def get_queryset(self):
        queryset = super(ListPerfil, self).get_queryset()
        queryset = queryset.get(pk=self.request.user.id)
        return queryset


class ListPerfis(ListView):
    model = Profile
    template_name = 'accounts/usuarios.html'
    context_object_name = 'perfil_list'


class CreatePerfil(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('contas:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(CreatePerfil, self).form_valid(form)


class UpdatePerfil(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('contas:list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        f = form.save(commit=False)
        password = form.cleaned_data['password']
        f.set_password(password)
        f.save()
        return super(UpdatePerfil, self).form_valid(form)


class PerfilDelete(DeleteView):
    model = Profile
    success_url = "/contas/usuarios/"


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            profiles = Profile.objects.all()
            data['html_profile_list'] = render_to_string('accounts/includes/partial_profile_list.html', {
                'profiles': profiles
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def profile_delete(request, pk):

    profile = get_object_or_404(Profile, pk=pk)
    data = dict()
    if request.method == 'POST' and request.user.is_superuser:
        profile.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        profiles = Profile.objects.all()
        data['html_list'] = render_to_string('accounts/includes/partial_profile_list.html', {
            'perfil_list': profiles
        })
    else:
        context = {'profile': profile}
        data['html_form'] = render_to_string('accounts/includes/partial_profile_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)
