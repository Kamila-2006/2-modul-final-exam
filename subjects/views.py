from django.shortcuts import render
from .models import Subject
from django.views.generic import ListView


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'