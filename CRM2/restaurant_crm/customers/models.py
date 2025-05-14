from django.db import models

class Customer(models.Model):
    LOYALTY_STATUS_CHOICES = [
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    loyalty_status = models.CharField(max_length=20, choices=LOYALTY_STATUS_CHOICES, default='bronze')

    def __str__(self):
        return self.name
