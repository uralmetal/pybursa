from django.contrib import admin

# Register your models here.

from .models import Lesson
from .models import Course

admin.site.register(Lesson)
admin.site.register(Course)