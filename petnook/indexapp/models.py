from django.db import models
from loginapp.models import CustomUser



class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)


    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    synopsis = models.TextField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='movies')
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)


    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('movie', 'user')  # Ensure a user can rate a movie only once

    def __str__(self):
        return f"{self.rating}/5 by {self.user.username} for {self.movie.title}"

