from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField(max_length=20)

    def __str__(self):
        return self.name