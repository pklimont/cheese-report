from typing import List
from Domain.product import Product




class Cart:
    def __init__(self, products: List[Product]):
        self.products = products

    def total(self) -> float:
        return sum(p.total_price() for p in self.products)

    def get_products(self) -> List[Product]:
        return self.products
