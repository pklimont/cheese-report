

class Product:
    def __init__(self, name:str, price_per_kg:float,quantity_kg:float=1.0):
        self.name = name
        self.price_per_kg = price_per_kg
        self.quantity_kg = quantity_kg

        def total_price() -> float:
            return self.price_per_kg * self.quantity_kg



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

for product in products:
    print(product.name, product.price_per_kg, product.quantity_kg)



