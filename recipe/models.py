from django.contrib.auth.models import User
from django.db import models


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    process = models.TextField()
    images = models.ImageField(upload_to="media/")
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.recipe_name


#from django.db import models

# Create your models here.
