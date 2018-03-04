from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class StuffView(TemplateView):
    template_name = 'stuff.html'
