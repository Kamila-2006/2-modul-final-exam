from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'