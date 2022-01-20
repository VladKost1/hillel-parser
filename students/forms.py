import re

from django import forms
from django.core.exceptions import ValidationError
from students.models import Teacher, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'age', 'subject', 'salary')

    def clean(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError('Only 18+')

        regex = r'^\+380\d{9}'
        phone = self.cleaned_data['phone']
        is_phone_number = re.match(regex, phone)
        if not is_phone_number:
            raise ValidationError('Phone number is not valid')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'age', 'average_rating', 'phone')

    def clean(self):
        regex = r'^\+380\d{9}'
        phone = self.cleaned_data['phone']
        is_phone_number = re.match(regex, phone)
        if not is_phone_number:
            raise ValidationError('Phone number is not valid')
