from django.contrib.auth.models import User
from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=20)
    # vencimento = models.DateField(verbose_name='vencimento',help_text='Dia do mes para um vencimento fixo')
    tipo = models.IntegerField(choices=((1, 'Entrada'), (2, 'Saida')))

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return u'/movimentacao/tipo/'


class Movimentacao(models.Model):

    cod_movimentacao = models.CharField(max_length=10, verbose_name='Código de Movimentação')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data de Lançamento')
    valor = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Usuario responsável', null=True, blank=True)
    tipo = models.ForeignKey(Tipo, verbose_name='Evento',
                             help_text='Evento refere-se a quaisquer tipo de transação de entrada e saida de capital.', null=True, blank=True)
    fonte_destino = models.CharField(max_length=20, verbose_name='Fonte/Destino', help_text='De onde veio ou para '
                                                                                            'onde foi o dinheiro '
                                                                                            'referente à transação.')
    observacao = models.TextField(max_length=400, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fonte_destino
