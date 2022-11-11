from typing import TypedDict


class User(TypedDict):
    id: str
    username: str
    shipping_address: str


def find_user_by_id(user_id: str) -> User:
    return {
        "id": user_id,
        "username": f"test_{user_id}",
        "shipping_address": "123 Main St",
    }
