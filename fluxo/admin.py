from django.contrib import admin

# Register your models here.
from fluxo.models import Movimentacao, Tipo

admin.site.register(Movimentacao)
admin.site.register(Tipo)