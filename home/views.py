from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pattern, Analogy, Riddle, IP
from .utils import save_client_ip

def home(request):
    save_client_ip(request)
    context = {
        'title': 'Home',
    }
    return render(request, 'home/home.html', context)

def about(request):
    save_client_ip(request)
    context = {
        'title': 'About',
    }
    return render(request, 'home/about.html', context)

def science(request):
    save_client_ip(request)
    context = {
        'title': 'Science',
    }
    return render(request, 'home/science.html', context)

@login_required
def program(request):
    save_client_ip(request)
    context = {
        'title': 'Program'
    }
    return render(request, 'home/program.html', context)

@login_required
def patterns(request):
    patterns  = Pattern.objects.filter(is_active=True)
    save_client_ip(request)
    context = {
        'title': 'Patterns',
        'patterns': patterns
    }

    return render(request, 'home/patterns.html', context)

@login_required
def analogies(request):
    analogies  = Analogy.objects.filter(is_active=True)
    save_client_ip(request)
    context = {
        'title': 'Analogies',
        'analogies': analogies
    }
    return render(request, 'home/analogies.html', context)

@login_required
def puzzles(request):
    save_client_ip(request)
    context = {
        'title': 'Puzzles',
    }
    return render(request, 'home/puzzles.html', context)

@login_required
def memory(request):
    save_client_ip(request)
    context = {
        'title': 'Memory',
    }
    return render(request, 'home/memory.html', context)

@login_required
def riddles(request):
    save_client_ip(request)
    riddles  = Riddle.objects.filter(is_active=True)
    context = {
        'title': 'Riddles',
        'riddles': riddles,
    }
    return render(request, 'home/riddles.html', context)