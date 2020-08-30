from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pattern, Analogy, Riddle

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

def program(request):
    context = {
        'title': 'Program'
    }
    return render(request, 'home/program.html', context)

def patterns(request):
    patterns  = Pattern.objects.filter(is_active=True)
    context = {
        'title': 'Patterns',
        'patterns': patterns
    }

    return render(request, 'home/patterns.html', context)

def analogies(request):
    analogies  = Analogy.objects.filter(is_active=True)
    context = {
        'title': 'Analogies',
        'analogies': analogies
    }
    return render(request, 'home/analogies.html', context)

def puzzles(request):
    context = {
        'title': 'Puzzles',
    }
    return render(request, 'home/puzzles.html', context)

def memory(request):
    context = {
        'title': 'Memory',
    }
    return render(request, 'home/memory.html', context)

def riddles(request):
    riddles  = Riddle.objects.filter(is_active=True)
    context = {
        'title': 'Riddles',
        'riddles': riddles,
    }
    return render(request, 'home/riddles.html', context)