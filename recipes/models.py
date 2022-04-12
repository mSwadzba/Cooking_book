from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_recpies')
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    commenting_users = models.ManyToManyField(User, through='Comment', related_name='commented_recipies')
    rating_users = models.ManyToManyField(User, through='Rating', related_name='rated_recipies')
    noting_users = models.ManyToManyField(User, through='Note', related_name='noted_recipies')


class Ingredient(models.Model):
    name = models.CharField(max_length=32)


class Unit(models.Model):
    name = models.CharField(max_length=32)


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    number_ingredient = models.IntegerField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    contents = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)


class Note(models.Model):
    contents = models.CharField(max_length=100)
    recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
