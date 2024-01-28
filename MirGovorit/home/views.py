from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Recipe, RecipeItems


def add_product_to_recipe(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        recipe_id = request.GET.get('recipe_id')
        weight = request.GET.get('weight')
        recipe = Recipe.objects.get(id=recipe_id)
        product = Product.objects.get(id=product_id)
        item, created = RecipeItems.objects.update_or_create(
            recipe=recipe, product=product, defaults={'weight': weight}
        )
        print(item, created)
        return JsonResponse({'status': 'success'})


def cook_recipe(requset):
    if requset.method == 'GET':
        recipe_id = requset.GET.get('recipe_id')
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            items = RecipeItems.objects.filter(recipe=recipe)
            for item in items:
                product = item.product
                product.count += 1
                product.save()
            return JsonResponse({'status': 'success'})
        except Recipe.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Recipe not found'})


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        recipes = Recipe.objects.exclude(
            items__product_id=product_id, items__weight__gte=10
        )
        return render(request, 'recipes_without_product.html', {'recipes': recipes})


def show_all(request):
    recipe_id = request.GET.get('recipe_id')
    recipe_items = RecipeItems.objects.filter(recipe_id=recipe_id).select_related('product', 'recipe')
    recipe_dict = {}
    for item in recipe_items:
        recipe_name = item.recipe.name
        product_name = item.product.name
        weight = item.weight
        if recipe_name not in recipe_dict:
            recipe_dict[recipe_name] = []
        recipe_dict[recipe_name].append(f"{product_name}: {weight}г")

    return render(request, 'recipes_without_product.html', {'recipe_all': recipe_dict})
