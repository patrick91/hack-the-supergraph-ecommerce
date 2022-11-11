from typing_extensions import Self

import strawberry

from api.common.types import Money
from data import products


@strawberry.federation.type(keys=["id"])
class Product:
    id: strawberry.ID
    title: str | None
    description: str | None
    media_url: str | None
    weight: float | None
    price: Money | None

    @classmethod
    def from_dict(cls, product: products.Product) -> Self:
        return cls(
            id=strawberry.ID(product["id"]),
            title=product["title"],
            description=product["description"],
            media_url=product["media_url"],
            weight=product["weight"],
            price=Money(
                amount=product["price"]["amount"],
                currency=product["price"]["currency"],
            ),
        )

    @classmethod
    def find_by_id(cls, id: strawberry.ID) -> Self | None:
        product = products.find_product_by_id(id)
        return None if product is None else cls.from_dict(product)

    @classmethod
    def resolve_reference(cls, id: strawberry.ID) -> Self:
        product = cls.find_by_id(id)

        if product is None:
            raise ValueError(f"Product with id {id} not found")

        return product


@strawberry.input
class ProductSearchInput:
    title_starts_with: str | None = strawberry.UNSET


@strawberry.type
class ProductsQuery:
    @strawberry.field
    def search_products(
        self, search_input: ProductSearchInput | None = None
    ) -> list[Product | None] | None:
        return [Product.from_dict(product) for product in products.get_all_products()]

    @strawberry.field
    def product(self, id: strawberry.ID) -> Product | None:
        return Product.find_by_id(id)
