from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django import forms

from .models import Course
from .models import Lesson

# Create your views here.

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)

def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/list.html', context)

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

def add(request):
    if request.method == 'POST':
        form_add = CourseModelForm(request.POST)
        if form_add.is_valid():
            instance = form_add.save()
            messages.success(request, "Курс успешно добавлен!")
            return redirect('/')
    else:
        form_add = CourseModelForm()
    context = {'form_add': form_add}
    return render(request, 'courses/add.html', context)

def edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form_edit = CourseModelForm(request.POST, instance=course)
        if form_edit.is_valid():
            instance = form_edit.save()
            messages.success(request, "Курс успешно отредактирован!")
            return redirect('courses:edit', course_id)
    else:
        form_edit = CourseModelForm(instance=course)
    context = {'form_edit': form_edit}
    return render(request, 'courses/edit.html', context)

def remove(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        course.delete()
        messages.success(request, "Курс успешно удалён!")
    except Exception:
        messages.success(request, "Курс успешно не найден")
    return redirect('/')