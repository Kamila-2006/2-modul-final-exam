from django.shortcuts import render
from .models import Group
from django.views.generic import ListView

class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'