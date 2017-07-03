from django.contrib import admin

# Register your models here.
from cliente.models import Cliente, Endereco

admin.site.register(Cliente)
admin.site.register(Endereco)
# admin.site.register(Servico)
