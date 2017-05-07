from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Kisi(models.Model):
    KisiID = models.IntegerField(primary_key=True)
    Adi = models.CharField(max_length=120, verbose_name='Adı')
    Soyadi = models.CharField(max_length=120, verbose_name='Soyadı')
    Resim = models.ImageField(null=True, blank=True)
    KullaniciID = models.IntegerField(verbose_name='Kullanıcı ID')

    def __str__(self):
        return self.Adi + ' ' + self.Soyadi


class KisiTelefon(models.Model):
    KisiTelefonID = models.IntegerField(primary_key=True, auto_created=True)
    Kisi = models.ForeignKey('Kisi', verbose_name='Kişi', related_name='Telefons')
    Telefon = models.CharField(max_length=13, verbose_name='Telefon')
    Tur = models.SmallIntegerField(verbose_name='Tür')


class KisiEposta(models.Model):
    KisiEpostaID = models.IntegerField(primary_key=True)
    Kisi = models.ForeignKey('Kisi', verbose_name='Kisi', related_name='Epostas')
    Eposta = models.CharField(max_length=150, verbose_name='Eposta')
    Tur = models.SmallIntegerField(verbose_name='Tür')
