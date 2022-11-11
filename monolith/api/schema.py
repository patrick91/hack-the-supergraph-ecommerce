import strawberry

from api.orders.query import OrdersQuery
from api.products.query import ProductsQuery
from api.users.query import UsersQuery


@strawberry.type
class Query(ProductsQuery, OrdersQuery, UsersQuery):
    pass


schema = strawberry.federation.Schema(
    Query,
    enable_federation_2=True,
)
