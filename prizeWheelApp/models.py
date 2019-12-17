from django.db import models

# Create your models here.


class Prize(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField()


class User(models.Model):
    phoneNumber = models.IntegerField()
    participated = models.BooleanField(default=False)
