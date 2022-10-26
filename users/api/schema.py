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
    price_high: float | None
    price_low: float | None
    items_in_order: int | None


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


@strawberry.type
class Query:
    @strawberry.field
    def viewer(self) -> User | None:
        return None


schema = strawberry.federation.Schema(
    Query,
    enable_federation_2=True,
)
