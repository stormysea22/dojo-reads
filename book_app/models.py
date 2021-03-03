from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(blank=True)
    user = models.ForeignKey(User, related_name="books_added", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=255)
    books = models.ForeignKey(Book, related_name="author", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    description = models.CharField(max_length=255)
    rating = models.IntegerField()
    reviewed_book = models.ForeignKey(Book, related_name="review", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="review_added", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


