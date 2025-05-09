from django.db import models

# Create your models here.
class Student(models.Model):
    name  = models.CharField(max_length=30, default='')
    grade = models.CharField(max_length=2, default='')

    def __str__(self):
        return self.name