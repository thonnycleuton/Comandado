import re
import datetime

from django.contrib.auth.models import User
from django.db import models

from accounts.choices import FUNCAO
from venda.models import ItensVenda


class Profile(User):

    foto = models.ImageField(upload_to='users', default='no-image-box.png', blank=True)
    funcao = models.IntegerField(choices=FUNCAO, default=None)
    telefone = models.CharField(max_length=15)
    meta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # data_nascimento = models.DateField()

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):

        self.telefone = re.sub(r'[^\d]+', '', self.telefone)
        return super(Profile, self).save(*args, **kwargs)

    def is_gerente(self):

        gerencia = Profile.objects.get(pk=self.pk).groups.filter(name='Gerência').exists()

        return gerencia

    def get_meta_semanal(self):

        return self.meta/4

    def get_rendimento(self, initial=None):

        faturamento = 0
        if initial is None:
            initial = datetime.date.today().replace(day=1)

        for vendas in ItensVenda.objects.filter(vendedor=self.id, cod_venda__data_venda__range=(initial, datetime.date.today() + datetime.timedelta(days=1))):

            if not vendas.cod_venda.comanda:
                faturamento += vendas.valor

        return faturamento

    def get_rendimento_diario(self):
        amount = self.get_rendimento(datetime.date.today())
        return amount

    def get_rendimento_semanal(self):
        segunda = datetime.date.today() - datetime.timedelta(datetime.date.today().weekday())
        return self.get_rendimento(segunda)

    def get_rendimento_porcentagem(self):

        rendimento = self.get_rendimento()
        porcentagem = 0

        try:
            porcentagem = (rendimento * 100)/self.meta
        except:
            pass

        return int(porcentagem)

    def get_rendimento_porcentagem_semanal(self):

        rendimento = self.get_rendimento_semanal()
        porcentagem = 0

        porcentagem = (rendimento * 100)/(self.meta/4)

        return int(porcentagem)
