from django.db import models


class Group(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=30
    )
    number_students = models.PositiveIntegerField(
        verbose_name='number students'
    )

    @property
    def full_group(self):
        return f'{self.name}, {self.number_students}'

    def __str__(self):
        return f'{self.name}, {self.number_students}'
