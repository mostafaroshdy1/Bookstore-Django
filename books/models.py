from django.db import models
from django.core import validators


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        validators=[
            validators.MinLengthValidator(10),
            validators.MaxLengthValidator(500),
        ]
    )
    rate = models.FloatField(
        validators=[validators.MaxValueValidator(10), validators.MinValueValidator(1)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
