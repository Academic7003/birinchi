from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic import ListView
from pages.models import PagesModel

class Main(ListView):
    model=PagesModel
    context_object_name='main_list'
    template_name='main.html'
    
