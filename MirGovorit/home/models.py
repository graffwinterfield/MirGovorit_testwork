from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)


class Recipe(models.Model):
    name = models.CharField(max_length=100)


class RecipeItems(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
