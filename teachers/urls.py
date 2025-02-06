from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('teachers-list/', views.TeacherListView.as_view(), name='list'),
]