from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Student
from django.views.generic import ListView
from django.views.generic import CreateView
from students.forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students/list')