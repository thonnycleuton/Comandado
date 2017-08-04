from django.contrib.auth.models import User
from django.db import models


class Profile(User):
    foto = models.ImageField(upload_to='users', default='no-image-box.png')
    funcao = models.CharField(max_length=150, default=None)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name
