from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),

    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
]
