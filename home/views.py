from django.shortcuts import render

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