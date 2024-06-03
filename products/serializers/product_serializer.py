from rest_framework import serializers
from products.models import ProductModel

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product model"""
    class Meta:
        model = ProductModel
        fields = "__all__"
