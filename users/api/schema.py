from typing_extensions import Self

import strawberry
from strawberry.federation.schema_directives import Key


@strawberry.federation.type(keys=[Key(fields="id", resolvable=False)])
class Order:
    id: strawberry.ID


@strawberry.federation.type(keys=[Key(fields="id", resolvable=False)])
class Product:
    id: strawberry.ID


@strawberry.input
class OrderFilters:
    order_id: strawberry.ID
    price_high: float | None = None
    price_low: float | None = None
    items_in_order: int | None = None


@strawberry.type
class Cart:
    items: list[Product | None] | None
    subtotal: float | None


@strawberry.federation.type(keys=["id"])
class User:
    id: strawberry.ID
    username: str
    cart: Cart | None
    shipping_address: str | None

    @strawberry.field
    def orders(self, filter: OrderFilters) -> list[Order | None] | None:
        return None

    @classmethod
    def resolve_reference(cls, id: strawberry.ID) -> Self:
        return User(
            id=id,
            username="test",
            cart=Cart(
                items=[
                    Product(id=strawberry.ID("1")),
                    Product(id=strawberry.ID("2")),
                ],
                subtotal=100.0,
            ),
            shipping_address="123 Main St",
        )


@strawberry.type
class Query:
    @strawberry.field
    def viewer(self) -> User | None:
        # TODO: maybe use headers to define user
        return User(
            id=strawberry.ID("1"),
            username="test",
            cart=Cart(
                items=[
                    Product(id=strawberry.ID("1")),
                    Product(id=strawberry.ID("2")),
                ],
                subtotal=100.0,
            ),
            shipping_address="123 Main St",
        )


schema = strawberry.federation.Schema(
    Query,
    enable_federation_2=True,
)
