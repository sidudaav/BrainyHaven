from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('program/', views.program, name='program'),
    path('science/', views.science, name='science'),
]