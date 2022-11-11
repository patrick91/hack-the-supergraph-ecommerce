from .products import ALL_PRODUCTS, Product


def get_cart_for_user(user_id: str) -> list[Product]:
    return [
        ALL_PRODUCTS[0],
        ALL_PRODUCTS[1],
    ]
