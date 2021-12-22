from django import forms
from django.core.exceptions import ValidationError
from students.models import Teacher, Student


class TeacherForm(forms.ModelForm):
    def clean(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError('Only 18+')

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'age', 'subject', 'salary')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'age', 'average_rating')
