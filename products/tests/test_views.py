from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import ProductModel
from products.serializers import ProductSerializer


class ProductListCreateViewTest(APITestCase):
    """Views Testing"""
    
    def setUp(self):
        self.product_data = {
            "title": "Test Product",
            "category": "Test Category",
            "price": 9.99,
            "description": "Test Description",
            "image": "http://dhamala.com/image.jpg",
            "rating_rate": 4.5,
            "rating_count": 10,
        }
        self.url = reverse("product_list_create")

    def test_create_product(self):
        response = self.client.post(self.url, self.product_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductModel.objects.count(), 1)
        self.assertEqual(ProductModel.objects.get().title, "Test Product")

    def test_list_products(self):
        ProductModel.objects.create(**self.product_data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_products_by_title(self):
        ProductModel.objects.create(**self.product_data)
        response = self.client.get(self.url, {"title": "Test Product"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_products_by_category(self):
        ProductModel.objects.create(**self.product_data)
        response = self.client.get(self.url, {"category": "Test Category"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ProductDetailUpdateDeleteViewTest(APITestCase):
    def setUp(self):
        self.product = ProductModel.objects.create(
            title="Test Product",
            category="Test Category",
            price=9.99,
            description="Test Description",
            image="http://dhamala.com/image.jpg",
            rating_rate=4.5,
            rating_count=10,
        )
        self.url = reverse(
            "product_detail_update_delete", kwargs={"id": self.product.id}
        )

    def test_retrieve_product(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.product.title)

    def test_update_product(self):
        updated_data = {
            "title": "Updated Product",
            "category": "Updated Category",
            "price": 19.99,
            "description": "Test Description Update",
            "image": "http://dhamala.com/image.jpg",
            "rating_rate": 3.5,
            "rating_count": 12,
        }
        response = self.client.put(self.url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.title, "Updated Product")

    def test_delete_product(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductModel.objects.count(), 0)
