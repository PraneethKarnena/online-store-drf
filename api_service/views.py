from django.shortcuts import render
from django.http import JsonResponse


def home_view(request):
    return JsonResponse({'success': True, 'message': 'Please view documentation at https://docs.google.com/document/d/17DkpOB_B37Zc5SlaAGtWiqZde1gTfLPqpQKdDbKvjgE/edit?usp=sharing'})