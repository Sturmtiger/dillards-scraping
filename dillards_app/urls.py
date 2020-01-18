from django.urls import path
from . import views


app_name = 'dillards'

urlpatterns = [
    path('', views.ParseProductsView.as_view(), name='parse_products'),
    path('parsed-products/', views.ProductsListView.as_view(), name='products_list'),
]
