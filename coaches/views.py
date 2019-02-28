from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Coach
from courses.models import Course

def detail(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    teacher = Course.objects.filter(coach=coach)
    assistant = Course.objects.filter(assistant=coach)
    context = {'coach': coach, 'teacher': teacher, 'assistant': assistant}
    return render(request, 'coaches/detail.html', context)