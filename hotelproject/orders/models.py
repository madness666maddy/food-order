from django.db import models
from menu.models import Food, Combo

class Order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
    ]

    customer_name = models.CharField(max_length=100)
    foods = models.ManyToManyField(Food, blank=True)
    combos = models.ManyToManyField(Combo, blank=True)
    total_amount = models.IntegerField()

    order_status = models.CharField(
    max_length=20,
    default='Pending'

    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

payment_id = models.CharField(max_length=100, blank=True, null=True)
payment_status = models.CharField(max_length=20, default='PENDING')
