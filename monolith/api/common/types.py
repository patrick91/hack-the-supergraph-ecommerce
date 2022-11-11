import strawberry


@strawberry.federation.type(shareable=True)
class Money:
    amount: float | None
    currency: str | None
