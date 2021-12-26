from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Group
from .forms import GroupForm


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', context={'groups': groups})


def create_groups(request):
    if request.method == 'GET':
        return render(request, 'create_groups.html', context={'form': GroupForm()})
    form = GroupForm(request.POST)
    form.save()
    return redirect(reverse('group_list'))
