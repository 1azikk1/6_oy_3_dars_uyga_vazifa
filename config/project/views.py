from django.shortcuts import render
from project.models import Course, Student


def home(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    return render(request, 'index.html', {'courses': courses, 'students': students})


