from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    FavoriteViewSet,
    IngredientViewSet,
    RecipeViewSet,
    ShoppingViewSet,
    TagViewSet,
    ListFollowViewSet,
    FollowViewSet,
    DownloadShopping
)

router = DefaultRouter()

router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)

urlpatterns = [
    path('users/subscriptions/',
         ListFollowViewSet.as_view(), name='subscriptions'),
    path('users/<int:author_id>/subscribe/',
         FollowViewSet.as_view(), name='subscribe'),
    path('recipes/download_shopping_cart/',
         DownloadShopping.as_view(), name='dowload_shopping'),
    path('recipes/<int:recipe_id>/favorite/',
         FavoriteViewSet.as_view(), name='favorite'),
    path('recipes/<int:recipe_id>/shopping/',
         ShoppingViewSet.as_view(), name='shopping'),
    path('', include(router.urls)),
]
