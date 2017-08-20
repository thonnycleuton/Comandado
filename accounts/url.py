from django.urls import reverse_lazy

from accounts.views import ListPerfil, ListPerfis, CreatePerfil, alterar_status, alterar_privilegio, PerfilDelete, \
    profile_delete, UpdatePerfil
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
    url(r'^$', ListPerfil.as_view(), name='perfil'),
    url(r'^usuarios/$', ListPerfis.as_view(), name='list'),
    url(r'^novo/$', CreatePerfil.as_view(), name='novo'),
    url(r'^delete/(?P<pk>\d+)/$', profile_delete, name='delete'),
    url(r'^alterar/(?P<pk>\d+)/$', UpdatePerfil.as_view(), name='alterar'),
    url(r'^alterar_privilegio/(?P<pk>\d+)/$', alterar_privilegio, name='alterar_privilegio'),
    url(r'^alterar_status/(?P<pk>\d+)/$', alterar_status, name='alterar_status'),

    # reset passwords
    # url(r'^password/$', password_change, {'template_name': 'accounts/registration/password.html', 'post_change_redirect': 'contas:perfil'}, name='password_change'),

    url(r'^change-password/$', PasswordChangeView.as_view(success_url=reverse_lazy('contas:perfil'), template_name='registration/password_change.html'), name='password_change'),
    url(r'^password_reset/$', PasswordResetView.as_view(email_template_name='registration/password_reset_email.html', template_name='registration/password_reset.html', ), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    url(r'^entrar/$', LoginView.as_view(), name='login'),
    url(r'^sair/$', LogoutView.as_view(), name='logout'),
]