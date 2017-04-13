from __future__ import unicode_literals

from django.db import models

# Create your models here.
from djmoney.models.fields import MoneyField


class TimeStamp(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#
# class Statusable(models.Model):
#     class Meta:
#         abstract = True
#
#     is_active = models.BooleanField(default=True)


class Addressable(models.Model):
    class Meta:
        abstract = True

    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.TextField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)


class Cliente(Addressable, TimeStamp):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)

    def __unicode__(self):
        return "%s" % self.nome


class Servico(TimeStamp):
    data = models.DateTimeField()
    valor = MoneyField(max_digits=10, decimal_places=2, default_currency='BRL')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
