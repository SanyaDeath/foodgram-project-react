from django_filters import rest_framework as filters

from .models import Recipe, Ingredient


class RecipeFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='receipttag__tag__slug')
    is_favorited = filters.BooleanFilter(method='get_favorite')
    is_in_shopping = filters.BooleanFilter(method='get_in_shopping')

    class Meta:
        model = Recipe
        fields = ('is_favorited', 'is_in_shopping', 'author', 'tags')

    def get_favorite(self, queryset, name, value):
        if value:
            return Recipe.objects.filter(favorites__user=self.request.user)
        return Recipe.objects.all()

    def get_in_shopping(self, queryset, name, value):
        if value:
            return Recipe.objects.filter(shopping__user=self.request.user)
        return Recipe.objects.all()


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Ingredient
        fields = ('name',)
