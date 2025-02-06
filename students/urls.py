from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('students-list/', views.StudentListView.as_view(), name='list'),
]