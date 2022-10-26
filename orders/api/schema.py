import strawberry
from strawberry.federation.schema_directives import Key


@strawberry.federation.type(shareable=True)
class Money:
    amount: float | None
    currency: str | None


@strawberry.federation.type(keys=[Key(fields="id", resolvable=False)])
class User:
    id: strawberry.ID


@strawberry.federation.type(keys=[Key(fields="id", resolvable=False)])
class Product:
    id: strawberry.ID


@strawberry.federation.type(keys=["id"])
class Order:
    id: strawberry.ID
    buyer: User
    items: list[Product]
    total: Money


@strawberry.type
class Query:
    @strawberry.field
    def order(self, id: strawberry.ID) -> Order | None:
        return Order(
            id=id,
            buyer=User(id=strawberry.ID("1")),
            items=[Product(id=strawberry.ID("1")), Product(id=strawberry.ID("2"))],
            total=Money(amount=100, currency="USD"),
        )


schema = strawberry.federation.Schema(
    Query,
    enable_federation_2=True,
)
