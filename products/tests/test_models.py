from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Category, Tag


class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test1234")
        self.category = Category.objects.create(
            name="Tools & Equipment", slug="tools-equipment"
        )
        self.tag = Tag.objects.create(name="Certified", slug="certified")
        self.product = Product.objects.create(
            name="Test Product 1",
            slug="test-product-1",
            description="Test description 1",
            price=15.00,
            created_by=self.user,
            stock=50,
        )
        self.product.categories.add(self.category)
        self.product.tags.add(self.tag)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product 1")
        self.assertEqual(self.product.slug, "test-product-1")
        self.assertEqual(self.product.price, 15.00)
        self.assertEqual(self.product.stock, 50)
        self.assertEqual(self.product.created_by.username, "test_user")
