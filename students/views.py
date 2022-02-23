from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from students.forms import TeacherForm, StudentForm
from students.models import Teacher, Student
from groups.models import Group
from rest_framework import generics

from students.serializers import StudentsListSerializer, StudentDetailSerializer, GroupsListSerializer, \
    GroupDetailSerializer


class StudentsList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsListSerializer


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer

    def get_object(self):
        return get_object_or_404(Student, pk=self.kwargs.get('student_id'))


class GroupsList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsListSerializer


class GroupDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupDetailSerializer

    def get_object(self):
        return get_object_or_404(Group, pk=self.kwargs.get('group_id'))


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', context={'students': students})


def create_student(request):
    if request.method == 'GET':
        return render(request, 'create_student.html', context={'form': StudentForm()})
    form = StudentForm(request.POST)
    form.save()
    return redirect(reverse('students_list'))


def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'GET':
        form = StudentForm(instance=student)
        return render(request, 'edit_student.html', context={'form': form, 'student': student})
    form = StudentForm(request.POST, instance=student)
    form.save()
    return redirect(reverse('students_list'))


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect(reverse('students_list'))


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers_list.html', context={'teachers': teachers})


def create_teachers(request):
    if request.method == 'GET':
        return render(request, 'create_teacher.html', context={'form': TeacherForm()})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teachers_list'))
    return HttpResponse(str(form.errors), status=400)


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, 'edit_teacher.html', context={'form': form, 'teacher': teacher})
    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
    return redirect(reverse('teachers_list'))


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect(reverse('teachers_list'))
