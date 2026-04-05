from Domain.product import Product
from Domain.cart import Cart
from Services.report_generator import ReportGenerator

products = [
    Product("Roquefort", 12.50,2.0),
    Product("Stilton", 11.24,1.0),
    Product("Brie", 9.30,1.0),
    Product("Gouda", 8.55,1.0),
    Product("Edam", 11.00,1.0),
    Product("Parmezan", 16.50,3.5),
    Product("Mozzarella", 14.00,0.13),
    Product("Ser owczy", 122.32,0.22),
    Product("Listek miętowy",20.00,0.20)
]

cart = Cart(products)
report=ReportGenerator.generate(cart)

print(report)
