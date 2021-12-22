from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(
        verbose_name='first name',
        max_length=64
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=64
    )
    age = models.PositiveIntegerField(
        verbose_name='age'
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_info(self):
        return f'{self.first_name} {self.last_name}, {self.age}'

    def __str__(self):
        return self.get_full_info()


class Teacher(Person):
    first_name = models.CharField(
        verbose_name='first name',
        max_length=64
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=64
    )
    age = models.PositiveIntegerField(
        verbose_name='age'
    )
    subject = models.CharField(
        verbose_name='subject',
        max_length=64
    )

    salary = models.CharField(
        verbose_name='salary',
        max_length=64
    )

    def get_job_info(self):
        return f'Subject: {self.subject}, salary: {self.salary}'


class Student(Person):
    average_rating = models.FloatField(
        verbose_name='average rating'
    )

    def get_student_info(self):
        return f'{self.first_name} {self.last_name} has {self.average_rating} rating'
