from django.urls import path
from .views.mainpanel import dashboard
from .views.products import product_list, product_create, product_edit, product_delete

urlpatterns = [
    path('', dashboard, name='admin_dashboard'),
    path('products/', product_list, name='admin_product_list'),
    path('products/add/', product_create, name='admin_product_create'),
    path('products/<int:pk>/edit/', product_edit, name='admin_product_edit'),
    path('products/<int:pk>/delete/', product_delete, name='admin_product_delete'),
]