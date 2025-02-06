from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('groups-list/', views.GroupListView.as_view(), name='list'),
]