from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import DepartmentForm
from .models import Department
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from subjects.models import Subject
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView


def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    subjects = Subject.objects.all()
    ctx = {
        'students':students,
        'teachers':teachers,
        'groups':groups,
        'subjects':subjects,
    }
    return render(request, 'dashboard.html', ctx)

class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'

class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'departments/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('departments:list')

class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'departments/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('departments:list')
    context_object_name = 'department'

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'

class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('departments:list')
    context_object_name = 'department'