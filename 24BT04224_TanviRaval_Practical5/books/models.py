from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    genre = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']