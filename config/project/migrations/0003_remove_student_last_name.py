# Generated by Django 5.1.4 on 2024-12-08 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_student_last_name_alter_course_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
    ]
