from rest_framework import serializers
from .models import *


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    size = serializers.StringRelatedField(many=True)
    color = ColorSerializer(many=True)
    shop = ShopSerializer(many=True)
    brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'
        read_only = "__all__"


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only = "__all__"
