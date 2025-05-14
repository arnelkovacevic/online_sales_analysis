from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, *products):
         # Dodavanje proizvoda
        for product in products:
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
            print("----------------------------")

    def display_total_value(self):
      # Prikaz ukupne vrednosti svih proizvoda.
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Ukupna vrijednost svih proizvoda: {total_value}€\n")


    def remove_product(self, product_name):
         #Uklanjanje proizvoda 
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Proizvod '{product_name}' je uspjesno uklonjen.")
                return
        print(f"Proizvod '{product_name}' nije pronadjen.")
