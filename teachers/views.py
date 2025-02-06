from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView
from django.views.generic import CreateView
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
    success_url = reverse_lazy('teachers/list')