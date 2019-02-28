from django.shortcuts import render
from django.http import HttpResponse

from math import sqrt
# Create your views here.

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def check_arg(index, is_a=False):
    if (index == None):
        return 'коэффициент не определён'
    if (is_int(index) == False):
        return 'коэффициент не целое число'
    if (is_a == True and int(index) == 0):
        return 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    return None

def calc(request):
    a = request.GET.get('a')
    a_view = check_arg(a, True)
    b = request.GET.get('b')
    b_view = check_arg(b)
    c = request.GET.get('c')
    c_view = check_arg(c)
    if (a_view == None and b_view == None and c_view == None):
        a = int(a)
        b = int(b)
        c = int(c)
        D = b * b - 4 * a * c
        if (D > 0):
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b + sqrt(D)) / (2 * a)
        elif (D == 0):
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = None
        else:
            x1 = None
            x2 = None
    else:
        D = None
        x1 = None
        x2 = None
    data = {"a": a, "a_view": a_view, "b": b, "b_view": b_view, "c": c, "c_view": c_view, "D": D, "x1": x1, "x2": x2}
    return render(request, 'quadratic/results.html', context=data)