from django.contrib import admin
from .views import Recipe, RecipeItems, Product


class RecipeModelAdmin(admin.ModelAdmin):
    model = Recipe

class ProductModelAdmin(admin.ModelAdmin):
    model = Product

class RecipeItemsModelAdmin(admin.ModelAdmin):
    model = RecipeItems

admin.site.register(Recipe, RecipeModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(RecipeItems, RecipeItemsModelAdmin)
