from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2000)
    justification = models.CharField(max_length=4000, null=True)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
