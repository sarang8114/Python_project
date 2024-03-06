from django.db import models

# Create your models here.


class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    organ_to_donate = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

