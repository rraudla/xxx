from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class mk(models.Model):
    maakond = models.CharField(max_length=20)

    def __str__(self):
        return self.maakond

class vald(models.Model):
    maakond = models.ForeignKey(mk, on_delete=models.CASCADE)
    vald = models.CharField(max_length=20)

    def __str__(self):
        return self.vald

class linn(models.Model):
    vald_id = models.ForeignKey(vald, on_delete=models.CASCADE)
    linn = models.CharField(max_length=20)

    def __str__(self):
        return self.linn

