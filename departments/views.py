from django.shortcuts import render
from .models import Department
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from subjects.models import Subject
from django.views.generic import ListView


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