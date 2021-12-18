import random

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from faker import Faker

from students.forms import TeachersForm, GroupsForm
from students.models import Student, Group



def student(request):
    teachers = Student.objects.all()
    groups = Group.objects.all()
    return render(request, 'students.html', context={'students': teachers, 'groups': groups})


@require_http_methods(['GET', 'POST'])
def create_teachers(request):
    if request.method == 'GET':
        fake = Faker()

        data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "age": random.randint(17, 60),
        }

        form = TeachersForm(initial=data)

        return render(request, 'create-teachers.html', context={'form': form})

    form = TeachersForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('students-list'))

    return HttpResponse(str(form.errors), status=400)


def create_groups(request):
    fake = Faker()
    data = {
        "name": fake.first_name(),
        "number": random.randint(1, 20),
    }
    form = GroupsForm(initial=data)
    if request.method == 'GET':
        return render(request, 'create-groups.html', context={'form': form})

    form = GroupsForm(request.POST)
    form.save()
    return HttpResponseRedirect(reverse('students-list'))
