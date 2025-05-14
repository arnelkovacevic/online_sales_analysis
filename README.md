# Online Sales Analysis

**Online Sales Analysis** je Python aplikacija koja omogućava upravljanje inventarom i korpom proizvoda.

---

## Opis klasa i funkcionalnosti:

### 1 **Product**
- Atributi:
  - `name`: Naziv proizvoda
  - `price`: Cena proizvoda
  - `quantity`: Količina proizvoda
- Metode:
  - `display_info()`: Ispisuje informacije o proizvodu
  - `update_quantity(new_quantity)`: Ažurira količinu proizvoda

### 2 **ProductManager**
- Atributi:
  - `products`: Lista svih dostupnih proizvoda
- Metode:
  - `add_product(*products)`: Dodaje proizvode u listu
  - `display_all_products()`: Prikazuje sve proizvode
  - `display_total_value()`: Prikazuje ukupnu vrednost svih proizvoda
  - `remove_product_by_name(name)`: Uklanja proizvod prema imenu

### 3 **Cart**
- Atributi:
  - `cart_items`: Lista proizvoda u korpi
- Metode:
  - `add_to_cart(product)`: Dodaje proizvod u korpu
  - `display_cart_items()`: Prikazuje proizvode u korpi
  - `calculate_total()`: Računa ukupnu vrednost korpe

---

## Pokretanje aplikacije
Pokreni aplikaciju sa:
```bash
python3 main.py
