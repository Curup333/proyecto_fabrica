from models import Product, Customer, Order

# Listado de productos
sofa_valery = Product("Valery", "sofa", 2500, 0, True)
sofa_kyoto = Product("Kyoto", "sofa", 3700, 8, True)
sofa_lucio = Product("Lucio", "sofa", 3500, 10, True)
chair_teresa = Product("Teresa", "chair", 300, 60, True)
chair_einstein = Product("Einstein", "chair", 400, 40, True)
armchair_harp = Product("Harp", "armchair", 1500, 10, True)
armchair_edsra = Product("Edsra", "armchair", 1200, 12, True)

# Cliente
customer = Customer("Dulce Maria", False)

# Procesar pedido
order = Order(customer)

order.add_item(sofa_valery, 1)
order.add_item(chair_teresa, 6)

total = order.calculate_total_price()
order.show_summary()
