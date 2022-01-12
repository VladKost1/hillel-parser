from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Group
from .forms import GroupForm, ContactForm
from school.settings import EMAIL_HOST_USER
from school.celery import send_email_task


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', context={'groups': groups})


def create_groups(request):
    if request.method == 'GET':
        return render(request, 'create_groups.html', context={'form': GroupForm()})
    form = GroupForm(request.POST)
    form.save()
    return redirect(reverse('group_list'))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_email_task.delay(form.cleaned_data['title'], form.cleaned_data['message'], EMAIL_HOST_USER,
                                  ['gorn228322@gmail.com'])
    return render(request, 'test_contact.html', context={'form': ContactForm()})
