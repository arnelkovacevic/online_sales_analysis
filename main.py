from product import Product
from product_manager import ProductManager

# Kreiranje ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
product1 = Product("Laptop", 1500, 3)
product2 = Product("Monitor", 300, 5)
product3 = Product("Mis", 25, 20)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikaz svih proizvoda
manager.display_all_products()

# Prikaz ukupne vrijdnosti svih proizvoda
manager.display_total_value()
