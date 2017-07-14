from __future__ import unicode_literals

from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cliente.models import Cliente
from servico.models import Servico


class Venda(models.Model):
    cod_venda = models.CharField(max_length=10, blank=True)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ManyToManyField(Servico, through='ItensVenda', through_fields=('cod_venda', 'cod_servico'), )
    data_venda = models.DateTimeField(auto_now=True)
    tipo = models.IntegerField(choices=((1, 'A vista'), (2, 'Prazo')))
    valor_venda = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __unicode__(self):
        return self.cod_venda


class ItensVenda(models.Model):
    cod_item = models.CharField(max_length=10, blank=True)
    cod_venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    cod_servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'itens'

    def __unicode__(self):
        return self.cod_item

    def save(self, *args, **kwargs):
        self.valor = Servico.objects.get(pk=self.cod_servico.id).valor
        super(ItensVenda, self).save(*args, **kwargs)