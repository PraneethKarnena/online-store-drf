from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view),
    path('authenticate/', views.authenticate), # Endpoint for obtaining Auth token

    path('category/', views.CategoryListView.as_view()), # Endpoint for creating and listing Categories
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view()), # Endpoint for RUD a single Cat

    path('product/', views.ProductListView.as_view()), # Endpoint for creating and listing Products
    path('product/<int:pk>/', views.ProductDetailView.as_view()) # Endpoint for RUD a single Product
]