from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Servico(models.Model):

    cod_servico = models.CharField(max_length=10)
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
