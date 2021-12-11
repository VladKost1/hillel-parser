from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.SmallIntegerField()

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}'
