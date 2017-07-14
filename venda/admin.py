from django.contrib import admin

# Register your models here.
from venda.models import Venda, ItensVenda


class ItensVendaInline(admin.TabularInline):
    model = ItensVenda
    extra = 1  # how many rows to show


class VendaClassAdmin(admin.ModelAdmin):
    inlines = (ItensVendaInline,)


admin.site.register(Venda, VendaClassAdmin)
admin.site.register(ItensVenda)
