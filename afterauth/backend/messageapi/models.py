from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length= 120)
    email = models.EmailField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        