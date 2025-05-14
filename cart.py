from product import Product

class Cart:
    def __init__(self):
        # Lista proizvoda u korpi
        self.cart_items = []

    def add_to_cart(self, product):
    # Dodavanje proizvoda u korpu
        self.cart_items.append(product)
        print(f"Proizvod '{product.name}' je dodat u korpu.")


    def total_cart_value(self):
        #Računanje ukupne vrednosti korpe
        total_value = sum(item.price * item.quantity for item in self.cart_items)
        return total_value

    def display_cart_items(self):
        #Prikaz proizvoda u korpi
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("\n---- Sadrzaj korpe ----")
            for item in self.cart_items:
                item.display_info()
            print(f"Ukupna vrijednost korpe: {self.total_cart_value()}€")
            print("--------------------------\n")
