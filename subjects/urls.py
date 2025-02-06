from django.urls import path
from . import views


app_name = 'subjects'

urlpatterns = [
    path('subjects-list/', views.SubjectListView.as_view(), name='list'),
]