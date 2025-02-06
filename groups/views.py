from django.shortcuts import render
from .models import Group
from django.views.generic import ListView
from django.views.generic import CreateView
from .forms import GroupForm
from django.urls import reverse_lazy


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'

class GroupCreateView(CreateView):
    model = Group
    template_name = 'groups/form.html'
    form_class = GroupForm
    success_url = reverse_lazy('groups/list')