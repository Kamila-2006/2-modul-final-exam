from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, UserLoginView, ProfileView
from django.views.generic import TemplateView


app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout-success/', TemplateView.as_view(template_name='users/logout.html'), name='logout_success'),
]