import strawberry
from strawberry.federation.schema_directives import Key


@strawberry.federation.type(keys=[Key(fields="id", resolvable=False)])
class User:
    id: strawberry.ID
    shipping_address: str | None = strawberry.federation.field(external=True)


@strawberry.federation.type(keys=[Key(fields="id", resolvable=False)])
class Product:
    id: strawberry.ID
    weight: float | None = strawberry.federation.field(external=True)


@strawberry.federation.type(keys=["id"])
class Order:
    id: strawberry.ID
    buyer: User = strawberry.federation.field(external=True)
    items: list[Product] = strawberry.federation.field(external=True)
    shipping_cost: float | None = strawberry.federation.field(
        requires=["items { weight }", "buyer { shippingAddress }"]
    )


schema = strawberry.federation.Schema(
    enable_federation_2=True,
)
