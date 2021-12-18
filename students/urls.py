from django.urls import path

from . import views

urlpatterns = [
    path('', views.student, name='students-list'),
    path('createT/', views.create_teachers, name='create-teachers'),
    path('createG/', views.create_groups, name='create-groups'),
]