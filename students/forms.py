from django import forms
from django.core.exceptions import ValidationError

from students.models import Group
from students.models import Student


class TeachersForm(forms.ModelForm):

    def clean(self):
        age = self.cleaned_data['age']

        if age < 18:
            raise ValidationError('Only 18+')

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
        )


class GroupsForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = (
            'name',
            'number'
        )