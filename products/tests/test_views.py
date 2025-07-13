from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Category, Tag


class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Tools & Equipment", slug="tools-equipment"
        )
        self.tag = Tag.objects.create(name="Certified", slug="certified")
        self.product = Product.objects.create(
            name="Digital Multimeter",
            slug="digital-multimeter",
            description="Professional multimeter for measuring voltage.",
            price=129.99,
            stock=50,
        )
        self.product.categories.add(self.category)
        self.product.tags.add(self.tag)

    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Digital Multimeter")
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_product_list_filtering(self):
        response = self.client.get(
            f"{reverse('product_list')}?category=tools-equipment"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Digital Multimeter")

        response = self.client.get(f"{reverse('product_list')}?tags=certified")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Digital Multimeter")

        response = self.client.get(f"{reverse('product_list')}?search=digital")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Digital Multimeter")

    def test_product_detail_view(self):
        url = reverse("product_detail", args=[self.product.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Digital Multimeter")
        self.assertContains(response, "129.99")
        self.assertTemplateUsed(response, "products/product_detail.html")
