import strawberry

from api.common.types import Money
from api.products.query import Product
from api.users.query import User


@strawberry.input
class OrderFilters:
    order_id: strawberry.ID
    price_high: float | None = None
    price_low: float | None = None
    items_in_order: int | None = None


@strawberry.federation.type(keys=["id"])
class Order:
    id: strawberry.ID
    buyer: User
    items: list[Product]
    total: Money


@strawberry.type
class OrdersQuery:
    @strawberry.field
    def order(self, id: strawberry.ID) -> Order | None:
        product_1 = Product.find_by_id(strawberry.ID("1"))
        product_2 = Product.find_by_id(strawberry.ID("2"))

        assert product_1 is not None
        assert product_2 is not None

        products = [product_1, product_2]

        total = 0.0

        for product in products:
            if product.price is not None:
                total += product.price.amount or 0

        buyer = User.find_by_id(strawberry.ID("1"))

        assert buyer is not None

        return Order(
            id=id,
            buyer=buyer,
            items=products,
            total=Money(amount=total, currency="USD"),
        )

    @strawberry.field
    def orders(self, filter: OrderFilters) -> list[Order | None] | None:
        return None
