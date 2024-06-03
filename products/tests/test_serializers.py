from rest_framework.test import APITestCase
from products.models import ProductModel
from products.serializers import ProductSerializer
from decimal import Decimal

class ProductSerializerTest(APITestCase):
    """Product Serializer Testing"""
    
    def setUp(self):
        self.product_attributes = {
            'title': 'Test Product',
            'price': Decimal('99.99'),
            'description': 'A product for testing.',
            'category': 'Test Category',
            'image': 'http://dhamala.com/image.jpg',
            'rating_rate': 4.5,
            'rating_count': 10
        }
        self.product = ProductModel.objects.create(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'title', 'price', 'description', 'category', 'image', 'rating_rate', 'rating_count'])

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.product_attributes['title'])

    def test_price_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['price'], str(self.product_attributes['price']))

    def test_description_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['description'], self.product_attributes['description'])

    def test_category_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['category'], self.product_attributes['category'])

    def test_image_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['image'], self.product_attributes['image'])

    def test_rating_rate_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['rating_rate'], self.product_attributes['rating_rate'])

    def test_rating_count_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['rating_count'], self.product_attributes['rating_count'])

    def test_deserialization(self):
        data = {
            'title': 'New Product',
            'price': '49.99',
            'description': 'Another test product.',
            'category': 'New Category',
            'image': 'http://dhamala.com/new_image.jpg',
            'rating_rate': 4.0,
            'rating_count': 5
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()
        self.assertEqual(product.title, data['title'])
        self.assertEqual(str(product.price), data['price'])
        self.assertEqual(product.description, data['description'])
        self.assertEqual(product.category, data['category'])
        self.assertEqual(product.image, data['image'])
        self.assertEqual(product.rating_rate, data['rating_rate'])
        self.assertEqual(product.rating_count, data['rating_count'])
