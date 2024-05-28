from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.services import ProductService

class ProductListView(APIView):
    def get(self, request):
        service = ProductService()
        products = service.get_all_products()
        return Response(products, status=status.HTTP_200_OK)
    
class ProductCreateView(APIView):
    def post(self, request):
        service = ProductService()
        product = service.create_product(request.data)
        if product:
            return Response(product, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)    

class ProductTitleSearchView(APIView):
    def get(self, request, title):
        service = ProductService()
        products = service.search_products_by_title(title)
        if products:
            return Response(products, status=status.HTTP_200_OK)
        return Response({"detail": "No products found"}, status=status.HTTP_404_NOT_FOUND)

class ProductDetailView(APIView):
    def get(self, request, id):
        service = ProductService()
        product = service.find_product_by_id(id)
        if product:
            return Response(product, status=status.HTTP_200_OK)
        return Response({"detail": "No product found"}, status=status.HTTP_404_NOT_FOUND)

class ProductCategoryFilterView(APIView):
    def get(self, request, category):
        service = ProductService()
        products = service.filter_products_by_category(category)
        if products:
            return Response(products, status=status.HTTP_200_OK)
        return Response({"detail": "No products found"}, status=status.HTTP_404_NOT_FOUND)

class ProductUpdateView(APIView):
    def put(self, request, id):
        service = ProductService()
        product = service.update_product(id, request.data)
        if product:
            return Response(product, status=status.HTTP_200_OK)
        return Response({"detail": "No product found or invalid data"}, status=status.HTTP_404_NOT_FOUND)

class ProductDeleteView(APIView):
    def delete(self, request, id):
        service = ProductService()
        result = service.delete_product(id)
        return Response(result, status=status.HTTP_200_OK)
