from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, default='')
    fbal = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name()