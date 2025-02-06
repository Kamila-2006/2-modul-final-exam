from django.urls import path
from . import views


app_name = 'departments'

urlpatterns = [
    path('departments-list/', views.DepartmentListView.as_view(), name='list'),
]