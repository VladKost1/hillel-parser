from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from group.models import Group


def group(request):
    group = Group.objects.all()
    data = serializers.serialize('json', group)
    return HttpResponse(data)


