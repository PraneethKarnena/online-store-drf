from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view),
    path('authenticate/', views.authenticate), # Endpoint for obtaining Auth token

    path('category/', views.CategoryListView.as_view()), # Endpoint for creating and listing categories
]