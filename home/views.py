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

@login_required
def program(request):
    context = {
        'title': 'Program'
    }
    return render(request, 'home/program.html', context)

@login_required
def patterns(request):
    patterns  = Pattern.objects.all()

    context = {
        'title': 'Patterns',
        'patterns': patterns
    }

    return render(request, 'home/patterns.html', context)

@login_required
def analogies(request):
    analogies  = Analogy.objects.all()

    context = {
        'title': 'Analogies',
        'analogies': analogies
    }
    return render(request, 'home/analogies.html', context)

@login_required
def puzzles(request):
    context = {
        'title': 'Puzzles',
    }
    return render(request, 'home/puzzles.html', context)

@login_required
def memory(request):
    context = {
        'title': 'Memory',
    }
    return render(request, 'home/memory.html', context)

@login_required
def riddles(request):
    riddles  = Riddle.objects.all()
    context = {
        'title': 'Riddles',
        'riddles': riddles,
    }
    return render(request, 'home/riddles.html', context)