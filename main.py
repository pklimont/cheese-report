from typing import List


class Product:
    def __init__(self, name:str, price_per_kg:float,quantity_kg:float=1.0):
        self.name = name
        self.price_per_kg = price_per_kg
        self.quantity_kg = quantity_kg

    def total_price(self) -> float:
            return self.price_per_kg * self.quantity_kg

class Cart:
    def __init__(self, products: List[Product]):
        self.products = products

    def total(self) -> float:
        return sum(p.total_price() for p in self.products)

    def get_products(self) -> List[Product]:
        return self.products

class ReportGenerator:
    def generate(self,cart:Cart) -> str:
        lines = ["RAPORT ZAKUPÓW SERÓW: \n"]

        for p in cart.get_products():
            lines.append(f"{p.name:15} {p.quantity_kg:.2f} kg * {p.price_per_kg:.2f} zł = {p.total_price():.2f} zł")

        lines.append(f"\nŁĄCZNA KWOTA: {cart.total():.2f} zł")
        return "\n".join(lines)






products = [
    Product("Roquefort", 12.50),
    Product("Stilton", 11.24),
    Product("Brie", 9.30),
    Product("Gouda", 8.55),
    Product("Edam", 11.00),
    Product("Parmezan", 16.50),
    Product("Mozzarella", 14.00),
    Product("Ser owczy", 122.32),
]



cart = Cart(products)
report = ReportGenerator().generate(cart)

print(report)









