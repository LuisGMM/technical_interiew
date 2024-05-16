from typing import List, Optional


class Review:
    def __init__(self, author: str, score: float, comment: str) -> None:
        self.author: str = author
        self.score: float = score
        self.comment: str = comment


class Product:
    def __init__(self, name: str, price: float, product_id: int) -> None:
        self.name: str = name
        self.price: float = price
        self.product_id: int = product_id
        self.reviews: List[Review] = []

    def add_review(self, review: Review) -> None:
        self.reviews.append(review)

    def get_average_score(self) -> float:
        if not self.reviews:
            return 0.0
        total_score: float = sum(review.score for review in self.reviews)

        return total_score / len(self.reviews)


class Order:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product: Product = product
        self.quantity: int = quantity


class InventoryManager:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add_product(self, name: str, price: float, product_id: int) -> Product:
        product = Product(name, price, product_id)
        self.products.append(product)

        return product

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None


class User:
    def __init__(self, username: str) -> None:
        self.username: str = username
        self.orders: List[Order] = []

    def place_order(self, product: Product, quantity: int) -> Order:
        order = Order(product, quantity)
        self.orders.append(order)

        return order
