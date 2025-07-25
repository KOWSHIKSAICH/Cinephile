from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')
    cast = models.TextField()
    director = models.CharField(max_length=100)
    music_director = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
