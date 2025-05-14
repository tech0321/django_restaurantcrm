from django.db import models

class InventoryItem(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} - {self.quantity} {self.unit}"
