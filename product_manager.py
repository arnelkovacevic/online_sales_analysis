from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
       # Dodavanje proizvoda u listu
        self.products.append(product)
        print(f"Proizvod '{product.name}' je uspjesno dodat.")

    def display_all_products(self):
       # Prikaz svih proizvoda u listi
        if not self.products:
            print("Nema dostupnih proizvoda.")
        else:
            print("\n---- Dostupni proizvodi ----")
            for product in self.products:
                product.display_info()
            print("----------------------------\n")

    def display_total_value(self):
      # Prikaz ukupne vrednosti svih proizvoda.
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Ukupna vrijednost svih proizvoda: {total_value}€")

