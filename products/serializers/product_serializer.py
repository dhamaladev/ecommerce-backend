from rest_framework import serializers
from products.models import ProductModel

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"
