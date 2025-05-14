from django.db import models
from customers.models import Customer

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='feedbacks')
    message = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.customer.name} - Rating: {self.rating}"
