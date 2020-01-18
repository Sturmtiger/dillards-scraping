from django.db import models


class ParsedProduct(models.Model):
    """Model for parsed data from `dillards.com`."""
    url = models.URLField()
    categories = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    colours = models.CharField(max_length=150)
    sizes = models.CharField(max_length=150)
    image_url = models.URLField()
    description = models.TextField()
