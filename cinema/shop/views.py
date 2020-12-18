from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .models import Movie

# Create your views here.
def home(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'index.html', context)