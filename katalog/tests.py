from django.test import TestCase
from django.urls import reverse, resolve
from katalog.models import CatalogItem  
from katalog.views import show_katalog

class CatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name="Gucci Horsebit 1955", 
            item_price=36000000, 
            item_stock=3,
            description="Original",
            rating=4,
            item_url="https://www.gucci.com/us/en/st/capsule/gucci-1955-horsebit-handbag")

    def test_models(self):
        gucci = CatalogItem.objects.get(item_name="Gucci Horsebit 1955")
        self.assertEquals(gucci.item_name, "Gucci Horsebit 1955")

class TestUrls(TestCase):
    def test_urls(self):
        url = reverse("katalog:show_katalog")
        self.assertEquals(resolve(url).func, show_katalog)

