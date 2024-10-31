from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ingredientDb(models.Model):
    ingredientId = models.IntegerField(primary_key=True)
    userName = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingredients')
    ingredientName = models.CharField(max_length=50)

class recipeDb(models.Model):
    recipeId = models.IntegerField(primary_key=True)
    userName = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recepies')
    recipeName = models.CharField(max_length=200)
    calories = models.IntegerField()
