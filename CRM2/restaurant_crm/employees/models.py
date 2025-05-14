from django.db import models

class Employee(models.Model):
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.role}"
