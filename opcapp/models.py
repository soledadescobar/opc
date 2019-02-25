from django.db import models

# Create your models here.
from django.db import models


class Variablesmacroeconomicas(models.Model):
    mes = models.DateField(primary_key=True)
    pibreal = models.BigIntegerField(blank=True, null=True)
    pibnominal = models.BigIntegerField()
    tc = models.FloatField(blank=True, null=True)
    factorestacionaidadexpo = models.FloatField(blank=True, null=True)
    factorestacionaidadimpo = models.FloatField(blank=True, null=True)
    estimacionexpo = models.FloatField(blank=True, null=True)
    estimacionimpo = models.FloatField(blank=True, null=True)
    estimacionexpodolares = models.FloatField(blank=True, null=True)
    estimacionimpodolares = models.FloatField(blank=True, null=True)
    estacionalidadpib = models.FloatField(blank=True, null=True)
    ipimensualizado = models.FloatField(blank=True, null=True)
    emaeso = models.FloatField(blank=True, null=True)
    emaese = models.FloatField(blank=True, null=True)
    ipcserie = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'variablesmacroeconomicas'


class Diashabiles(models.Model):
    mes = models.DateField(primary_key=True)
    diashabiles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'diashabiles'


class Serieipc(models.Model):
    mes = models.IntegerField()
    anio = models.IntegerField()
    variacionmensual = models.FloatField(blank=True, null=True)
    nivelgeneralipcnacional = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serieipc'
        unique_together = (('anio', 'mes'),)

    def __str__(self):
        return 'Mes: ' + str(self.anio) + '-' + str(self.mes)
