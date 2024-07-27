import factory
from factory.django import DjangoModelFactory

from core.apps.products.models.products import Product as ProductDTO


class ProductModelFactory(DjangoModelFactory):
    class Meta:
        model = ProductDTO

    title = factory.Faker("first_name")
    description = factory.Faker("text")
    price = 100
    is_visible = True
