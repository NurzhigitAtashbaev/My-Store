from django.urls import path
from .views import ProductList, ProductCreate, CategoryList



urlpatterns = [
    path('list/',ProductList.as_view(), name='product-list'),
    path('create/', ProductCreate.as_view(), name='product-create'),
    path('category-list/', CategoryList.as_view(), name='category-list'),
]