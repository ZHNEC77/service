from django.urls import path
from .views import product_list, product_detail, decrease_quantity

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/decrease_quantity/', decrease_quantity, name='decrease_quantity'),
]