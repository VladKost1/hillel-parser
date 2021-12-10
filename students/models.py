from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()

    def get_full_info(self):
        return f"{self.first_name} {self.last_name}, {self.age}"

    def __str__(self):
        return self.get_full_info()
