from django.db import models

# Create your models here.
from cliente.models import Cliente


class Agenda(models.Model):

    customer = models.ForeignKey(Cliente)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.start_time
