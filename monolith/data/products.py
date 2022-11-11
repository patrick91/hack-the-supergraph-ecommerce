from typing import TypedDict


class Price(TypedDict):
    amount: float
    currency: str


class Product(TypedDict):
    id: str
    title: str | None
    description: str | None
    media_url: str | None
    weight: float | None
    price: Price


ALL_PRODUCTS: list[Product] = [
    {
        "id": str(i),
        "title": f"Product {i}",
        "description": f"Product {i} Description",
        "media_url": f"https://example.com/product-{i}.jpg",
        "weight": 1.0 * i,
        "price": {
            "amount": 1.0 * i,
            "currency": "USD",
        },
    }
    for i in range(1, 10)
]


def get_all_products() -> list[Product]:
    return ALL_PRODUCTS


def find_product_by_id(id: str) -> Product | None:
    return next((product for product in ALL_PRODUCTS if product["id"] == id), None)
