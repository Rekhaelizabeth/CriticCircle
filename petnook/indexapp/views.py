from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Director, Movie,Rating,Review
from django.db.models import Avg


# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def seller(request):
    return render(request,'seller.html')
def sellerpage(request):
    return render(request,'sellerpage.html')

def productdescription(request,movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    # Check if the user has already rated or reviewed this movie
    user_rating = Rating.objects.filter(movie=movie, user=request.user).first()
    user_review = Review.objects.filter(movie=movie, user=request.user).first()

    # Calculate average rating
    average_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        rating_value = request.POST.get('rating')

        if review_text and not user_review:
            # Save the new review
            Review.objects.create(movie=movie, user=request.user, review_text=review_text)

        if rating_value and not user_rating:
            # Save the new rating
            Rating.objects.create(movie=movie, user=request.user, rating=int(rating_value))

        return redirect('movie_detail', movie_id=movie.id)

    context = {
        'movie': movie,
        'average_rating': average_rating,
        'reviews': movie.reviews.all(),
        'user_review': user_review,
        'user_rating': user_rating,
    }
    return render(request,'productdescription.html',context)
def movies(request):
    
    movie_list = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movie_list})

def directors(request):
    
    directorslist = Director.objects.all()  # Fetch only 3 movies
    return render(request, 'directors.html', {'directorslist': directorslist})
def director_movies(request, director_id):
    # Fetch the director based on the ID
    director = get_object_or_404(Director, id=director_id)
    # Fetch all movies by this director
    movies = Movie.objects.filter(director=director)
    context = {
        'director': director,
        'movies': movies,
    }
    return render(request, 'director_movies.html', context)


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Rating
from django.db.models import Avg

@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    # Check if the user has already rated or reviewed this movie
    user_rating = Rating.objects.filter(movie=movie, user=request.user).first()
    user_review = Review.objects.filter(movie=movie, user=request.user).first()

    # Calculate average rating
    average_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        rating_value = request.POST.get('rating')

        if review_text and not user_review:
            # Save the new review
            Review.objects.create(movie=movie, user=request.user, review_text=review_text)

        if rating_value and not user_rating:
            # Save the new rating
            Rating.objects.create(movie=movie, user=request.user, rating=int(rating_value))

        return redirect('movie_detail', movie_id=movie.id)

    context = {
        'movie': movie,
        'average_rating': average_rating,
        'reviews': movie.reviews.all(),
        'user_review': user_review,
        'user_rating': user_rating,
    }
    return render(request, 'movie_detail.html', context)


