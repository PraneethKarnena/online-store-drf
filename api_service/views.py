"""
Contains all the business logic for the API service
"""

from django.http import JsonResponse
from django.contrib.auth import authenticate as django_authenticate

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(['POST'])
def authenticate(request):
    """
    Obtain Token by authenticating against username and password
    """
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = django_authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            data = {'success': True, 'data': token.key}
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            raise Exception('Invalid credentials!')
    except Exception as e:
        data = {'success': False, 'message': f'Error: {str(e)}'}
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)


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


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):

    """
    Read/Update/Delete a single product category
    """

    permission_classes = [permissions.IsAuthenticated]

    queryset = models.ProductCategoryModel.objects.all()
    serializer_class = serializers.ProductCategorySerializer