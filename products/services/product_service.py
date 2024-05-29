from django.shortcuts import get_object_or_404
from products.models import ProductModel
from products.serializers import ProductSerializer

class ProductService:

    def get_all_products(self):
        products = ProductModel.objects.all()
        return ProductSerializer(products, many=True).data

    def create_product(self, data):
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return {'errors': serializer.errors}

    def find_product_by_id(self, id):
        try:
            product = ProductModel.objects.get(id=id)
            return ProductSerializer(product).data
        except ProductModel.DoesNotExist:
            return None

    def search_products_by_title(self, title):
        products = ProductModel.objects.filter(title__icontains=title)
        return ProductSerializer(products, many=True).data if products else None

    def filter_products_by_category(self, category):
        products = ProductModel.objects.filter(category__icontains=category)
        return ProductSerializer(products, many=True).data if products else None

    def update_product(self, id, data):
        try:
            product = ProductModel.objects.get(id=id)
        except ProductModel.DoesNotExist:
            return None
        serializer = ProductSerializer(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return {'errors': serializer.errors}

    def delete_product(self, id):
        product = get_object_or_404(ProductModel, id=id)
        product.delete()
        return {"status": "deleted"}
