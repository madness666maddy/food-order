from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Combo(models.Model):
    combo_name = models.CharField(max_length=100)
    foods = models.ManyToManyField(Food)
    combo_price = models.IntegerField()

    def __str__(self):
        return self.combo_name
