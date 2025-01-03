from django.db import models
from datetime import datetime
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=2000 ,unique=True)
    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now , blank = True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return f"{self.user} : {self.value[:50]}"
    

