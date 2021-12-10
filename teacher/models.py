from django.db import models


class Teachers(models.Model):
    Firs_name = models.CharField(max_length=10)
    Last_name = models.CharField(max_length=15)
    qualification = models.BigIntegerField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.qualification
# Create your models here.
