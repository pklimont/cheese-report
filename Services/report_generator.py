from Domain.cart import Cart





class ReportGenerator:
    @staticmethod
    def generate(cart:Cart) -> str:
        lines = ["RAPORT ZAKUPÓW SERÓW: \n"]

        for p in cart.get_products():
            lines.append(f"{p.name:15} {p.quantity_kg:.2f} kg * {p.price_per_kg:.2f} zł = {p.total_price():.2f} zł")

        lines.append(f"\nŁĄCZNA KWOTA: {cart.total():.2f} zł")
        return "\n".join(lines)

