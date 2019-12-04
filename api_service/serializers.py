from rest_framework import serializers

from . import models


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductCategoryModel
        fields = '__all__'
