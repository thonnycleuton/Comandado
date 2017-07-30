from accounts.views import ListPerfil, ListPerfis, CreatePerfil, alterar_status, alterar_privilegio, PerfilDelete, \
    profile_delete
from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_reset, password_reset_confirm, \
    password_reset_complete, password_reset_done

urlpatterns = [
    url(r'^$', ListPerfil.as_view(), name='perfil'),
    url(r'^usuarios/$', ListPerfis.as_view(), name='list'),
    url(r'^novo/$', CreatePerfil.as_view(), name='novo'),
    url(r'^delete/(?P<pk>\d+)/$', profile_delete, name='delete'),
    url(r'^alterar_privilegio/(?P<pk>\d+)/$', alterar_privilegio, name='alterar_privilegio'),
    url(r'^alterar_status/(?P<pk>\d+)/$', alterar_status, name='alterar_status'),
    url(r'^password/$', password_change, {'template_name': 'accounts/registration/password.html', 'post_change_redirect': 'contas:perfil'}, name='password_change'),
    url(r'^password_reset/$', password_reset,   {'template_name': 'accounts/registration/password_reset.html', 'post_reset_redirect': 'contas:password_reset_done'}, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, {'template_name': 'accounts/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, {'template_name': 'accounts/registration/password_reset_confirm.html', 'post_reset_redirect': 'contas:login'}, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
    url(r'^entrar/$', login, {'template_name': 'accounts/registration/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'home'}, name='logout'),
]