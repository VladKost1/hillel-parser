from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'number_students',)


class ContactForm(forms.Form):
    title = forms.CharField(max_length=20)
    message = forms.CharField(max_length=200)
    email = forms.CharField(max_length=20)
