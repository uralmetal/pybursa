from django.shortcuts import render
from django.views import generic
# Create your views here.

class ContacsView(generic.TemplateView):
    template_name = 'contacs/contacs.html'