from django.db import models


class Course(models.Model):
    objects = None
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    course_photo = models.ImageField(upload_to='posts/photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, default='example@gmail.com')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

