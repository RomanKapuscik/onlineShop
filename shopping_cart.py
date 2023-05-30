from typing import List
from item_database import get_price


class ShoppingCart:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.items: List[str] = []

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError('Too many items in the cart')
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self) -> float:
        total_price = 0.0
        for item in self.items:
            total_price += get_price(item)
        return total_price



