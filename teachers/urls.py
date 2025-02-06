from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('teachers-list/', views.TeacherListView.as_view(), name='list'),
    path('teacher-create/', views.TeacherCreateView.as_view(), name='create'),
]