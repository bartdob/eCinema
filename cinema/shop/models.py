from django.db import models
from django.utils import timezone

class Movie(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='products/')
    price = models.FloatField()
    year = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name