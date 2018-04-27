from django.db import models


class World(models.Model):
    created = models.DateField(auto_now=True)


class Game(models.Model):
    world = models.ForeignKey(World, on_delete=models.CASCADE)