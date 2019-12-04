"""
Contains all the business logic for the API service
"""

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import permissions

from . import models
from . import serializers


def home_view(request):
    """Home page - return some info"""
    return JsonResponse({'success': True, 'message': 'Please view documentation at https://docs.google.com/document/d/17DkpOB_B37Zc5SlaAGtWiqZde1gTfLPqpQKdDbKvjgE/edit?usp=sharing'})


class CategoryListView(generics.ListCreateAPIView):

    """
    List all product categories or create one
    """

    permission_classes = [permissions.IsAuthenticated]

    queryset = models.ProductCategoryModel.objects.all()
    serializer_class = serializers.ProductCategorySerializer
