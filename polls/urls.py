""" Modulo para definicao de rotas do app"""
from django.urls import path
from .views import index, data, conversor

# URLS Config do app
# Define a relacao entre um path e uma view
urlpatterns = [
   path('', index, name='home'),

   # 2. Definir a url
   path('data/', data, name='data_view'),

   path('conversor/', conversor, name='conversor'),

]