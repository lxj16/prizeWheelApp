from django.db import models

# Create your models here.


class Prize(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    phoneNumber = models.CharField(max_length=10,primary_key=True, unique=True)
    rolled = models.BooleanField(default=False)

    def __str__(self):
        return f'User with phone number {self.phoneNumber} is already participated'


class Winner(models.Model):
    phoneNumber = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    prize = models.ForeignKey(Prize, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Winner with phone number: {self.userID} won a prize with id: {self.prizeID }'
