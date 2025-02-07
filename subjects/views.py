from django.shortcuts import render
from .models import Subject
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import SubjectForm


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'

class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:list')

class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:list')
    context_object_name = 'subject'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects:list')
    context_object_name = 'subject'