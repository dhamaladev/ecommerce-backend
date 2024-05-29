from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from products.services import ProductService
from products.serializers import ProductSerializer
from products.models import ProductModel

class ProductListCreateView(generics.ListCreateAPIView):
    """Api view for create and list the products"""
    serializer_class = ProductSerializer
    service = ProductService()

    def get_queryset(self):
        queryset = ProductModel.objects.all()
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        if title:
            queryset = self.service.search_products_by_title(title)
        elif category:
            queryset = self.service.filter_products_by_category(category)
        return queryset

    def create(self, request, *args, **kwargs):
        product = self.service.create_product(request.data)
        if 'errors' in product:
            return Response(product, status=status.HTTP_400_BAD_REQUEST)
        return Response(product, status=status.HTTP_201_CREATED)

class ProductDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Api view for retrieve , update and delete products"""
    serializer_class = ProductSerializer
    lookup_field = 'id'
    service = ProductService()

    def get_queryset(self):
        return ProductModel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        product = self.service.find_product_by_id(kwargs['id'])
        if product is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(product, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        product = self.service.update_product(kwargs['id'], request.data)
        if product is None:
            return Response({"detail": "Not found or invalid data."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(product, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        result = self.service.delete_product(kwargs['id'])
        return Response(result, status=status.HTTP_200_OK)
