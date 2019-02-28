from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

# Create your views here.
from .models import Student
from courses.models import Course

class StudentDetailView(generic.DetailView):
    template_name = 'students/detail.html'
    model = Student

class StudentListView(generic.ListView):
    template_name = 'students/list.html'
    model = Student
    context_object_name = 'student_list'

    def get_queryset(self):
        try:
            course_id = int(self.request.GET.get('course_id'))
            course = Course.objects.get(pk=course_id)
            return Student.objects.filter(courses=course)
        except Exception:
            return Student.objects.all()

class StudentCreateView(generic.CreateView):
    template_name = 'students/add.html'
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        ret = super().form_valid(form)
        if ret.url == self.get_success_url():
            messages.success(self.request, "Студень успешно добавлен")
        return ret

class StudentUploadView(generic.UpdateView):
    template_name = 'students/edit.html'
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        ret = super().form_valid(form)
        if ret.url == self.get_success_url():
            messages.success(self.request, "Студень успешно отредактирован")
        return ret

class StudentDeleteView(generic.DeleteView):
    template_name = 'students/delete.html'
    model = Student
    success_url = reverse_lazy('students:list')

