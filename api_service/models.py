from django.db import models
from django.contrib.auth.models import User


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=6, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f'{self.code} - {self.name}'


class ProductModel(models.Model):

    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, null=False, blank=False)

    serial_num = models.CharField(max_length=12, null=False, blank=False, unique=True)

    manufacturer_name = models.CharField(max_length=255, null=False, blank=False)
    manufacturing_date = models.DateField(null=False, blank=False)

    stock = models.PositiveSmallIntegerField(null=False, blank=False, default=0)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, \
    related_name='product_creations')
    last_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, \
    related_name='product_updations')

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.name} - {self.description}'