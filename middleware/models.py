from django.db import models


class Logger(models.Model):
    path = models.CharField(
        verbose_name='path',
        max_length=64
    )

    method = models.CharField(
        verbose_name='method',
        max_length=64
    )

    execution_time = models.CharField(
        verbose_name='execution time',
        max_length=64
    )

    created = models.DateTimeField(
        verbose_name='date created',
        auto_now_add=True
    )
