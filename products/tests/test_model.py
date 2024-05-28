from django.test import TestCase
from products.models import ProductModel


class ProductModelTest(TestCase):

    def test_create_product(self):
        product = ProductModel.objects.create(
            title="test title",
            price=100,
            category="test category",
            image="test image",
            description="test description",
            rating_rate=10,
            rating_count=1000,
        )
        self.assertEqual(product.title, "test title")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.category, "test category")
        self.assertEqual(product.image, "test image")
        self.assertEqual(product.description, "test description")
        self.assertEqual(product.rating_rate, 10)
        self.assertEqual(product.rating_count, 1000)
