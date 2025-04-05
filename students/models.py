from django.db import models

# Create your models here.

class Student(models.Model):
    Student_name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    course_name = models.CharField(max_length=100)
    year = models.IntegerField()  # Year 1, 2, 3, 4

    def __str__(self):
        return self.name


