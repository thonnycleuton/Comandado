import re
from django.contrib.auth.models import User
from django.db import models

from accounts.choices import FUNCAO


class Profile(User):

    foto = models.ImageField(upload_to='users', default='no-image-box.png', blank=True)
    funcao = models.IntegerField(choices=FUNCAO, default=None)
    telefone = models.CharField(max_length=15)
    # data_nascimento = models.DateField()

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):

        self.telefone = re.sub(r'[^\d]+', '', self.telefone)
        return super(Profile, self).save(*args, **kwargs)
