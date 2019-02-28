from django.db import models

from coaches.models import Coach

class Course(models.Model):
    name = models.CharField(max_length=40)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='coach_courses',
                              related_query_name='coach_course', blank=True, null=True)
    assistant = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='assistant_courses',
                              related_query_name='assistant_course', blank=True, null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=40)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject