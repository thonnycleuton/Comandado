from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cliente.models import Cliente
from servico.models import Servico


class Venda(models.Model):

    cod_venda = models.TextField(max_length=10)
    cod_cliente = models.ForeignKey(Cliente)
    cod_servico = models.ForeignKey(Servico)
    data_venda = models.DateTimeField(auto_now=True)
    tipo = models.IntegerField(choices=((1, 'A vista'), (2, 'Prazo')))
    valor_venda = models.FloatField()
    vendedor = models.ForeignKey(User)

    class Meta:
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __unicode__(self):
        return self.cod_venda

    def save(self, *args, **kwargs):

        valor = Servico.objects.get(cod_servico=self.cod_servico.cod_servico).valor
        self.valor_venda = valor
        super(Venda, self).save(*args, **kwargs)

