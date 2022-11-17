from django.urls import path
from .views import index, games, cadastro, shopping

urlpatterns = [
    path('', index, name='index'),
    path('games', games, name='games'),
    path('cadastro', cadastro, name='cadastro'),
    path('shopping', shopping, name='shopping') 
]
