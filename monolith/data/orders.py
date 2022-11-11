from typing import TypedDict


class Order(TypedDict):
    id: str
    buyer_id: str
    item_ids: list[str]


ALL_ORDERS: list[Order] = [
    {
        "id": str(i),
        "buyer_id": "1",
        "item_ids": ["1", "2"],
    }
    for i in range(1, 10)
]


def find_order_for_buyer(buyer_id: str) -> list[Order]:
    return [order for order in ALL_ORDERS if order["buyer_id"] == buyer_id]
