from Domain import *
from Services.report_generator import ReportGenerator

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
report=ReportGenerator.generate(cart)

print(report)
