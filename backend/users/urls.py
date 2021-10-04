from django.urls import path, include

from djoser import views


# from .views import CustomAuthToken, Logout

urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/token/login/',
         views.TokenCreateView.as_view(), name='login'),
    path('auth/token/logout/',
         views.TokenDestroyView.as_view(), name='logout'),
]
