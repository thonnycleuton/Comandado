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


class Cliente(models.Model):
    cod_cliente = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    sexo = models.CharField(max_length=10)
    nacimento = models.DateField()
    estado_civil = models.CharField(max_length=20)
    status_ativo = models.BooleanField()
    endereco = models.ManyToManyField(Endereco)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __unicode__(self):
        return self.nome


class Servico(models.Model):
    cod_servico = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    valor = models.FloatField()
    foto = models.ImageField()
    status_ativo = models.BooleanField()

    class Meta:
        verbose_name = 'servico'
        verbose_name_plural = 'servicos'

    def __unicode__(self):
        return self.nome


class Fornecedor(models.Model):
    cod_fornecedor = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=250)
    inscricao_estadual = models.CharField(max_length=100)
    inscricao_municipal = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    status_ativo = models.BooleanField()

    class Meta:
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

    def __unicode__(self):
        return self.nome_fantasia


class Produto(models.Model):
    cod_produto = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    valor = models.FloatField()
    foto = models.ImageField()
    status_ativo = models.BooleanField()

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __unicode__(self):
        return self.nome
