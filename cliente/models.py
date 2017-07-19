# encoding=utf-8
from __future__ import unicode_literals

from django.db import models


class Endereco(models.Model):
    nome = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'endereco'
        verbose_name_plural = 'enderecos'

    def __unicode__(self):
        return self.nome


# Create your models here.
class Cliente(models.Model):

    cod_cliente = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    sexo = models.IntegerField(choices=((1, 'Feminino'), (2, 'Masculino'), (3, 'Outros')))
    nascimento = models.DateField()
    foto = models.ImageField(upload_to='cliente')
    estado_civil = models.IntegerField(choices=((1, 'Solteiro'), (2, 'Casado'), (3, 'Outros')), default=1)
    comanda = models.BooleanField(default=False)
    status_ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nome

    def get_gasto_total(self):
        from venda.models import Venda

        valor = 0
        for item in Venda.objects.filter(cod_cliente=self.pk):
            valor += item.valor_venda
        return valor
