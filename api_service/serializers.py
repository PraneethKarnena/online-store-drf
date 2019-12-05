from rest_framework import serializers

from . import models


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductCategoryModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='created_by.username')
    last_updated_by = serializers.ReadOnlyField(source='last_updated_by.username')

    category = ProductCategorySerializer(many=False)

    class Meta:
        model = models.ProductModel
        fields = '__all__'
