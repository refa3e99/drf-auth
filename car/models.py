from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(max_length=256)
    desc = models.TextField()

    def __str__(self):
        return self.name