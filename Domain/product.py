class Product:
    def __init__(self, name:str, price_per_kg:float,quantity_kg:float=1.0):
        self.name = name
        self.price_per_kg = price_per_kg
        self.quantity_kg = quantity_kg

    def total_price(self) -> float:
            return self.price_per_kg * self.quantity_kg