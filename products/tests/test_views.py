from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from products.models import ProductModel
from products.serializers import ProductSerializer
from decimal import Decimal

class ProductViewsTest(APITestCase):

    def setUp(self):
        self.product_data = {
            'title': 'Test Product',
            'price': Decimal('99.99'),
            'description': 'A product for testing.',
            'category': 'Test Category',
            'image': 'http://example.com/image.jpg',
            'rating_rate': 4.5,
            'rating_count': 10
        }
        self.product = ProductModel.objects.create(**self.product_data)
        self.product_url = reverse('product_detail', kwargs={'id': self.product.id})
        self.product_list_url = reverse('all_products')
        self.product_create_url = reverse('create_product')
        self.product_search_url = reverse('product_search', kwargs={'title': self.product_data['title']})
        self.product_category_url = reverse('product_category_filter', kwargs={'category': self.product_data['category']})
        self.product_update_url = reverse('product_update', kwargs={'id': self.product.id})
        self.product_delete_url = reverse('product_delete', kwargs={'id': self.product.id})

    def test_get_all_products(self):
        response = self.client.get(self.product_list_url)
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        new_product_data = {
            'title': 'New Product',
            'price': '49.99',
            'description': 'Another test product.',
            'category': 'New Category',
            'image': 'http://example.com/new_image.jpg',
            'rating_rate': 4.0,
            'rating_count': 5
        }
        response = self.client.post(self.product_create_url, new_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductModel.objects.count(), 2)
        self.assertEqual(ProductModel.objects.get(id=response.data['id']).title, new_product_data['title'])

    def test_search_product_by_title(self):
        response = self.client.get(self.product_search_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.product_data['title'])

    def test_get_product_detail(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.product_data['title'])

    def test_filter_product_by_category(self):
        response = self.client.get(self.product_category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category'], self.product_data['category'])

    def test_update_product(self):
        updated_product_data = {
            'title': 'Updated Product',
            'price': '59.99',
            'description': 'Updated test product.',
            'category': 'Updated Category',
            'image': 'http://example.com/updated_image.jpg',
            'rating_rate': 4.8,
            'rating_count': 20
        }
        response = self.client.put(self.product_update_url, updated_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_product = ProductModel.objects.get(id=self.product.id)
        self.assertEqual(updated_product.title, updated_product_data['title'])

    def test_delete_product(self):
        response = self.client.delete(self.product_delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductModel.objects.count(), 0)
