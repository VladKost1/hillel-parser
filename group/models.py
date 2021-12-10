from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30)
    rank = models.CharField(max_length=30)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.name
# Create your models here.
