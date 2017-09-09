# encoding=utf-8

from __future__ import unicode_literals

import datetime
from django.db import models

from servico.choices import CATEGORIA_SERVICOS


class Servico(models.Model):
    cod_servico = models.CharField(max_length=10, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    foto = models.ImageField(upload_to='servico', blank=True, default='no-image-box.png')
    status_ativo = models.BooleanField()
    categoria = models.IntegerField(choices=CATEGORIA_SERVICOS)

    class Meta:
        verbose_name = 'servico'
        verbose_name_plural = 'serviços'
        ordering = ('categoria',)

    def __str__(self):
        return str(self.nome) + " - (" + str(self.valor) + ")"

    def get_faturamento(self):
        from venda.models import ItensVenda
        valor_total = 0
        itens = ItensVenda.objects.filter(cod_servico=self.pk)
        for item in itens:
            valor_total += item.valor
        return valor_total

    def save(self, *args, **kwargs):

        if self.cod_servico is "":
            ultimo = '000' if Servico.objects.last() is None else Servico.objects.last().cod_servico[-3:]
            ultimo = str(int(ultimo) + 1)

            while len(ultimo) < 3:
                ultimo = "0" + ultimo
            self.cod_servico = "S" + ultimo

        return super(Servico, self).save(*args, **kwargs)
