from django.db import models


class Telefon(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    memorija = models.CharField(max_length=20)
    boja = models.CharField(max_length=20)
    cena = models.IntegerField()

    def __str__(self):
        return self.model       

class Ocena(models.Model):
    idTelefona = models.ForeignKey(Telefon, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    ocena = models.IntegerField()

    def __str__(self):
        return self.ocena
