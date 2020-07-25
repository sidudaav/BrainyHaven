from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home/home.html', context)

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'home/about.html', context)

def science(request):
    context = {
        'title': 'Science',
    }
    return render(request, 'home/science.html', context)

@login_required
def program(request):
    context = {
        'title': 'Program',
    }
    return render(request, 'home/program.html', context)