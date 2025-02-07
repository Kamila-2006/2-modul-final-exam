from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Student
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from students.forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')
    context_object_name = 'student'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    context_object_name = 'student'