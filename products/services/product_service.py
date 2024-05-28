from django.shortcuts import get_object_or_404
from products.models import ProductModel
from products.serializers import ProductSerializer

# product service
class ProductService:

# get all products
    def get_all_products(self):
        products = ProductModel.objects.all()
        return ProductSerializer(products, many=True).data

# create a new product
    def create_product(self, data):
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

# get product by id 
    def find_product_by_id(self, id):
        try:
            product = ProductModel.objects.get(id=id)
            return ProductSerializer(product).data
        except ProductModel.DoesNotExist:
            return None

# search products by title
    def search_products_by_title(self, title):
        products = ProductModel.objects.filter(title__icontains=title)
        return ProductSerializer(products, many=True).data if products else None

# filter products by category
    def filter_products_by_category(self, category):
        products = ProductModel.objects.filter(category=category)
        return ProductSerializer(products, many=True).data if products else None

# update product by id
    def update_product(self, id, data):
        product = ProductModel.objects.get(id = id)
        if not product:
            return None
        serializer = ProductSerializer(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            print(serializer.errors)
            return None

#delete a product
    def delete_product(self, id):
        product = get_object_or_404(ProductModel, id=id)
        product.delete()
        return {"status": "deleted"}
