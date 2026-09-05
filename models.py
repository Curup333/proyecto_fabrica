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
            print(f"- {self.name} available: {self.stock}")
            return True
        print(f"x {self.name} not available: {self.stock}")
        return False

    def reduce_stock(self, amount):
        if self.validate_stock(amount):
            self.stock -= amount
            return True
        return False

    def get_info(self):
        return f"Name: {self.name} - {self.category} - ${self.unit_price:.2f} | Stock: {self.stock}"


class Customer:
    def __init__(self, name, is_vip=False):
        self.name = name
        self.is_vip = is_vip

    def calculate_discount(self, total_price):
        if self.is_vip and total_price >= 5000:
            return 0.20
        elif self.is_vip:
            return 0.15
        elif total_price >= 1000:
            return 0.05
        return 0

    def apply_discount(self, total_price):
        discount = self.calculate_discount(total_price)
        if discount > 0:
            print(f"\nDiscount: {discount * 100:.2f}%")
        return total_price * (1 - discount)


class Order:
    def __init__(self, customer, items=None):
        self.customer = customer
        self.items = items or []
        self.rejected_items = []
        self.total_price = 0

    def add_item(self, product, amount):
        if product.reduce_stock(amount):
            self.items.append({
                "product": product,
                "amount": amount
            })
            return True
        self.rejected_items.append({
            "product": product,
            "amount": amount,
            "reason": "Out of stock"
        })
        return False

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
        print(f"Type: {'VIP' if self.customer.is_vip else 'Regular'}")
        print("\nITEMS:")
        for item in self.items:
            print(f" - {item['product'].name} x {item['amount']} | Unitary price: ${item['product'].unit_price:.2f} - Subtotal: ${item['product'].unit_price * item['amount']:.2f}")
        print(f"\nTOTAL: ${self.total_price:.2f}")

        if self.rejected_items:
            print("\nREJECTED ITEMS:")
            for item in self.rejected_items:
                print(f" - {item['product'].name} x {item['amount']} | Reason: {item['reason']}")

        if not self.items:
            print("\nNo items to show")

