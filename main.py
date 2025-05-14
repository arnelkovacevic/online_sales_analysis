from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiranje ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
product1 = Product("Laptop", 1500, 3)
product2 = Product("Monitor", 300, 5)
product3 = Product("Mis", 25, 20)
product4 = Product("Tastatura", 50, 20)

manager.add_product(product1, product2, product3, product4)


# Prikaz svih proizvoda
manager.display_all_products()

# Prikaz ukupne vrijednosti svih proizvoda
manager.display_total_value()

# Kreiranje instance Cart
cart = Cart()

# Dodavanje proizvoda u korpu iz liste dostupnih proizvoda
cart.add_to_cart(manager.products[0])  
cart.add_to_cart(manager.products[1])  
cart.add_to_cart(manager.products[3])  

# Prikaz proizvoda u korpi
cart.display_cart_items()
