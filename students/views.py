from random import randint

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from faker import Faker

from students.models import Student


def index(request):
    return HttpResponse('<h1>Hello django!!!</h1>')


def student(request):
    a = Faker()
    student = Student.objects.create(first_name=a.first_name(), last_name=a.last_name(), age=randint(0, 50))
    data = serializers.serialize('json', [student], fields=('id', 'first_name', 'last_name', 'age'))
    return HttpResponse(data)


def students(request):
    a = Faker()
    students = []
    res = request.GET.get('count')
    if res:
        for i in range(int(res)):
            student = Student.objects.create(first_name=a.first_name(), last_name=a.last_name(), age=randint(0, 50))
            students.append(student)
        data = serializers.serialize('json', students, fields=('id', 'first_name', 'last_name', 'age'))
        return HttpResponse(data)
    return HttpResponse('Error')

# student = Student.objects.create(first_name=a.first_name(), last_name=a.last_name(), age=randint(0, 20))
# result = serializers.serialize('json', [student, ], fields=('id', 'first_name', 'last_name', 'age'))
# return HttpResponse(result)
