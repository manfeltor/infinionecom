from django.urls import path
from .views import products

urlpatterns = [
    path('prodcuts', products, name='products'),
]