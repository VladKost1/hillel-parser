# Generated by Django 3.2.9 on 2022-01-24 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20220119_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.teacher'),
        ),
    ]
