from django.contrib.auth.models import User
from django.db import models

from accounts.choices import FUNCAO


class Profile(User):

    foto = models.ImageField(upload_to='users', default='no-image-box.png')
    funcao = models.IntegerField(choices=FUNCAO, default=None)
    telefone = models.CharField(max_length=11)
    # data_nascimento = models.DateField()

    def __str__(self):
        return self.first_name
