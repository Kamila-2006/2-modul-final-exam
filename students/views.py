from django.shortcuts import render
from .models import Student
from django.views.generic import ListView


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'