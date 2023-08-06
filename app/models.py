from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    std = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


