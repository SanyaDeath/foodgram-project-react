from django.contrib import admin

from .models import Favorite, Ingredient, Recipe, Shopping, Shopping_Cart, Tag


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('author', 'name', 'image', 'text', 'cooking_time')
    readonly_fields = ('pub_date',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('name', 'color', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ('name', 'measure_unit')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe', 'added_date')
    search_fields = ('user', 'recipe')


@admin.register(Shopping_Cart)
class Shopping_CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe', 'added_date')
    search_fields = ('user', 'recipe')
