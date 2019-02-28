from django.db import models

from courses.models import Course
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=70)
    skype = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name + ' ' + self.surname