from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all().order_by('-id')  # Show newest movies at the top
    return render(request, 'reviews/index.html', {'movies': movies})
