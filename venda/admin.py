from django.contrib import admin

# Register your models here.
from venda.models import Venda, ItensVenda

admin.site.register(Venda)
admin.site.register(ItensVenda)