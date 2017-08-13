# encoding=utf-8
from __future__ import unicode_literals

import re

from datetime import date
from django.db import models
from cliente.choices import *


class Endereco(models.Model):
    """
        Esta classe é responsável por modelar todos os tipos de endereços usados pelo sistema,
        donde a mesma possui um campo ForeingKey para um Cliente.

    """
    tipo = models.IntegerField(choices=TIPO)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.IntegerField(choices=CIDADES, default=20)
    estado = models.IntegerField(choices=ESTADOS, blank=True, default=10)
    referencia = models.CharField(max_length=100, blank=True)
    cliente = models.ForeignKey('Cliente')

    class Meta:
        verbose_name = 'endereco'
        verbose_name_plural = 'enderecos'

    def __str__(self):
        return self.cliente.nome + " - " + str(self.tipo)


# Create your models here.
class Cliente(models.Model):
    cod_cliente = models.CharField(max_length=10, null=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=14)
    sexo = models.IntegerField(choices=((1, 'Feminino'), (2, 'Masculino'), (3, 'Outros')))
    nascimento = models.DateField()
    estado_civil = models.IntegerField(choices=((1, 'Solteiro'), (2, 'Casado'), (3, 'Outros')), default=1)
    comanda = models.BooleanField(default=False, blank=True)
    status_ativo = models.BooleanField(default=True)
    # contatos
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    foto = models.ImageField(upload_to='cliente', default='no-image-box.png', blank=True)

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

    def get_idade(self):
        idade = date.today().year - self.nascimento.year
        print(idade)
        return idade

    def save(self, *args, **kwargs):
        if self.cod_cliente is "":
            ultimo = '000' if Cliente.objects.last() is None else Cliente.objects.last().cod_cliente[-3:]
            ultimo = str(int(ultimo) + 1)

            while len(ultimo) < 3:
                ultimo = "0" + ultimo
            self.cod_cliente = "C" + ultimo

        self.cpf = re.sub(r'[^\d]+', '', self.cpf)
        self.telefone = re.sub(r'[^\d]+', '', self.telefone)

        return super(Cliente, self).save(*args, **kwargs)
