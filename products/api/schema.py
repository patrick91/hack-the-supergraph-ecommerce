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
        return None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str) -> str:
        return name


schema = strawberry.federation.Schema(
    Query,
    Mutation,
    enable_federation_2=True,
)
