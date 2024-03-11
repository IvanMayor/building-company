from django.db import models


class Building(models.Model):
    building_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    floors = models.IntegerField()
