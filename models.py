# proyecto para gestion de producto en fabrica de muebles

class Product:
    def __init__(self, name, category, unit_price, stock=0, active=True):
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.stock = stock
        self.active = active

    def validate_stock(self, amount):
        if self.stock >= amount:
            print(f"- {self.name} disponible: {self.stock}")
            return True
        print(f"x {self.name} no disponible: {self.stock}")
        return False

    def reduce_stock(self, amount):
        if self.validate_stock(amount):
            self.stock -= amount
            return True
        return False

    def get_info(self):
        return f"Name: {self.name} - {self.category} - ${self.unit_price:.2f} | Stock: {self.stock}"

# Lista de productos
sofa_valery = Product("Valery", "sofa", 2500, 6, True)
sofa_kyoto = Product("Kyoto", "sofa", 3700, 8, True)
sofa_lucio = Product("Lucio", "sofa", 3500, 10, True)
chair_teresa = Product("Tereza", "chair", 300, 60, True)
chair_einstein = Product("Einstein", "chair", 400, 40, True)
armchair_harp = Product("Harp", "armchair", 1500, 10, True)
armchair_edsra = Product("Edsra", "armchair", 1200, 12, True)


class Customer:
    def __init__(self, name, its_vip=False):
        self.name = name
        self.its_vip = its_vip

    def calculate_discount(self, total_price):
        if self.its_vip and total_price >= 5000:
            return 0.20
        elif self.its_vip:
            return 0.15
        elif total_price >= 1000:
            return 0.05
        return 0

    def apply_discount(self, total_price):
        discount = self.calculate_discount(total_price)
        if discount > 0:
            print(f"Discount: {discount * 100:.2f}%")
        return total_price * (1 - discount)


class Order:
    def __init__(self, customer, items=None):
        self.customer = customer
        self.items = items or []
        self.total_price = 0

    def add_item(self, product, amount):
        self.items.append({
            "product": product,
            "amount": amount
        })

    def calculate_total_price(self):
        self.total_price = 0
        for item in self.items:
            subtotal = item["product"].unit_price * item["amount"]
            self.total_price += subtotal

        self.total_price = self.customer.apply_discount(self.total_price)
        return self.total_price

    def show_summary(self):
        print("\n========== Order Summary ==========")
        print(f"Customer: {self.customer.name}")
        print(f"Type: {self.customer.its_vip and 'VIP' or 'Regular'}")
        print("\nITEMS:")
        for item in self.items:
            print(f" {item['product'].name} x {item['amount']}")
        print(f"\nTOTAL: ${self.total_price:.2f}")

