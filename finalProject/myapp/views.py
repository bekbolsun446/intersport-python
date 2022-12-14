from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class ProductsListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        try:
            return Product.objects.filter(brand_id=self.kwargs['cat_id'])
        except:
            return Product.objects.all()


class CategoriesListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoriesListAPIView(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        try:
            return SubCategory.objects.filter(category_id=self.kwargs['pk'])
        except:
            return SubCategory.objects.all()
