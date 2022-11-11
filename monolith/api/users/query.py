import strawberry

from typing import Self

from api.products.query import Product
from data import users


@strawberry.type
class Cart:
    items: list[Product | None] | None
    subtotal: float | None


@strawberry.federation.type(keys=["id"])
class User:
    id: strawberry.ID
    username: str
    shipping_address: str | None

    @strawberry.field
    def cart(self) -> Cart | None:
        product_1 = Product.find_by_id(strawberry.ID("1"))
        product_2 = Product.find_by_id(strawberry.ID("2"))

        assert product_1 is not None
        assert product_2 is not None

        subtotal = 0.0

        if product_1.price is not None:
            subtotal += product_1.price.amount or 0

        if product_2.price is not None:
            subtotal += product_2.price.amount or 0

        return Cart(
            items=[product_1, product_2],
            subtotal=subtotal,
        )

    @classmethod
    def from_dict(cls, user: users.User) -> Self:
        return cls(
            id=strawberry.ID(user["id"]),
            username=user["username"],
            shipping_address=user["shipping_address"],
        )

    @classmethod
    def find_by_id(cls, id: strawberry.ID) -> Self | None:
        user = users.find_user_by_id(id)
        return None if user is None else cls.from_dict(user)


@strawberry.type
class UsersQuery:
    @strawberry.field
    def viewer(self) -> User | None:
        # TODO: maybe use headers to define user
        return User(
            id=strawberry.ID("1"),
            username="test",
            shipping_address="123 Main St",
        )
