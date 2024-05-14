from django.contrib.gis.db import models


class polygon(models.Model):
    name = models.CharField(max_length=50, null=True)
    poly = models.PolygonField(null=True)

    def __str__(self):
        return f' Polygone: {self.name}'


class node(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return f' Node: {self.name}'





