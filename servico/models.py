from __future__ import unicode_literals

import datetime
from django.db import models


class Servico(models.Model):
    cod_servico = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    foto = models.ImageField(upload_to='servico', blank=True)
    status_ativo = models.BooleanField()

    class Meta:
        verbose_name = 'servico'
        verbose_name_plural = 'servicos'

    def __unicode__(self):
        return self.nome

    def get_faturamento(self):
        from venda.models import Venda
        valor_total = 0
        vendas = Venda.objects.filter(servico=self.pk)
        for venda in vendas:
            valor_total += venda.valor_venda
        return valor_total

    def save(self, *args, **kwargs):
        ultimo = '000' if Servico.objects.last().cod_servico[-3:] is None or "" else Servico.objects.last().cod_servico[-3:]
        ultimo = str(int(ultimo) + 1)

        while len(ultimo) < 3:
            ultimo = "0" + ultimo
        self.cod_servico = "S" + ultimo
        return super(Servico, self).save(*args, **kwargs)
