from django.urls import path
from . import views

urlpatterns = [
    path('', views.groups_list, name='group_list'),
    path('create/', views.create_groups, name='create_group'),
]
