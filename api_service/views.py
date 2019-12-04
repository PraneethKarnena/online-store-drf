from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics

from . import models
from . import serializers

def home_view(request):
    return JsonResponse({'success': True, 'message': 'Please view documentation at https://docs.google.com/document/d/17DkpOB_B37Zc5SlaAGtWiqZde1gTfLPqpQKdDbKvjgE/edit?usp=sharing'})


class CategoryListView(generics.ListCreateAPIView):
    queryset = models.ProductCategoryModel.objects.all()
    serializer_class = serializers.ProductCategorySerializer