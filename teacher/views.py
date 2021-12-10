from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from group.models import Group


def teachers(request):
    teachers = Group.objects.all()
    data = serializers.serialize('json', teachers)
    return HttpResponse(data)
# Create your views here.
