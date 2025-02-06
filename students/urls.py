from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('students-list/', views.StudentListView.as_view(), name='list'),
    path('student-create/', views.StudentCreateView.as_view(), name='create'),
]