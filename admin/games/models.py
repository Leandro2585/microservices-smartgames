from django.db import models

class Game(models.Model):
    title = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    quantity_in_cart = models.PositiveIntegerField(default = 0)
    price = models.PositiveIntegerField(default = 200)

class User(models.Model):
    pass