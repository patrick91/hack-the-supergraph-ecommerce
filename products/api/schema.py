from typing_extensions import Self

import strawberry


@strawberry.federation.type(shareable=True)
class Money:
    amount: float | None
    currency: str | None


@strawberry.federation.type(keys=["id"])
class Product:
    id: strawberry.ID
    title: str | None
    description: str | None
    media_url: str | None
    weight: float | None
    price: Money | None

    @classmethod
    def resolve_reference(cls, id: strawberry.ID) -> Self:
        return cls(
            id=id,
            title="Product Title",
            description="Product Description",
            media_url="https://example.com/product.jpg",
            weight=1.0,
            price=Money(amount=1.0, currency="USD"),
        )


@strawberry.input
class ProductSearchInput:
    title_starts_with: str | None = strawberry.UNSET


@strawberry.type
class Query:
    @strawberry.field
    def search_products(
        self, search_input: ProductSearchInput | None = None
    ) -> list[Product | None] | None:
        return []

    @strawberry.field
    def product(self, id: strawberry.ID) -> Product | None:
        return Product(
            id=id,
            title="Product Title",
            description="Product Description",
            media_url="https://example.com/product.jpg",
            weight=1.0,
            price=Money(amount=1.0, currency="USD"),
        )


schema = strawberry.federation.Schema(
    Query,
    enable_federation_2=True,
)
