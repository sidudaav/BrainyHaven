from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('science/', views.science, name='science'),
    path('program/', views.program, name='program'),
    path('patterns/', views.patterns, name='patterns'),
    path('analogies/', views.analogies, name='analogies'),
    path('memory/', views.memory, name='memory'),
    path('puzzles/', views.puzzles, name='puzzles'),
]