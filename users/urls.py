from django.urls import path
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from . forms import RegisterForm
from . import views

app_name = 'users'

urlpatterns = [
	path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=AuthenticationForm), name='login'),
	path('register/', views.register_account, name='register'),
	path('logout/', views.logout_view, name='logout'),
]	

