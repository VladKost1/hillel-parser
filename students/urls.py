from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('students/', views.students_list, name='students_list'),
    path('create_student/', views.create_student, name='create_student'),
    path('create_teacher/', views.create_teachers, name='create_teacher'),
    path('edit_teacher/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('rest_students/', views.StudentsList.as_view(), name='students_list'),
    path('rest_students/<int:student_id>/', views.StudentDetails.as_view(), name='students_details'),
    path('rest_groups/', views.GroupsList.as_view(), name='groups_list'),
    path('rest_groups/<int:group_id>/', views.GroupDetails.as_view(), name='groups_details'),
]

