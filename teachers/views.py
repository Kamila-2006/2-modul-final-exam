from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import TeacherForm


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teachers/form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')
    context_object_name = 'teacher'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    context_object_name = 'teacher'