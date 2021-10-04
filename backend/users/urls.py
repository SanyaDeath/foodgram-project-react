from django.urls import path, include

# from djoser import views


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authoken')),
]
