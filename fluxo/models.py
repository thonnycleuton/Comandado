from django.db import models


# Create your models here.
from accounts.models import Profile


class Tipo(models.Model):
    nome = models.CharField(max_length=20)
    vencimento = models.DateField(verbose_name='vencimento')
    tipo = models.IntegerField(choices=((1, 'Entrada'), (2, 'Saida')))


class Movimentacao(models.Model):

    cod_movimentacao = models.CharField(max_length=10, verbose_name='Código de Movimentação')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data de Lançamento')
    valor = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')
    user = models.ForeignKey(Profile, verbose_name='Usuario responsável')
    tipo = models.ForeignKey(Tipo, verbose_name='Evento')
