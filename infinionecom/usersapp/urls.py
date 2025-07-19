from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login_redirect.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]