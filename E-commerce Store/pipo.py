class ProductManager:
    def __init__(self, products = []):
        self.products = products

    def load_products(self, filename):
        # Just learnt this, opens and closes the file by itself
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                price = float(data[1])
                stock = int(data[2])

                # Adding the product to the products list
                product = Product(name, price, stock)
                self.products.append(product)

    def save_products(self, filename):
        with open(filename, 'w') as file:
            for product in self.products:
                line = f"{product.name},{product.price},{product.stock}\n"
                file.write(line)


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_in_stock(self):
        return self.stock > 0
    
    # I can do this in the add_product function
    # def update_stock(self, quantity):
    #     if quantity <= self.stock:
    #         self.stock -= quantity
    #     else:
    #         print("Not enough stock, go away.")
        

class Cart:
    def __init__(self, items = {}):
        self.items = items # dict to store product names as keys and prices as values
    
    def add_product(self, product, quantity=1):
        if quantity > product.stock:
            print(f"Go away! We only have {product.stock} of {product.name}.")
        else:
            if product in self.items:
                self.items[product] += quantity  # add quantity to existing product
            else:
                self.items[product] = quantity  # add new product
            product.stock -= quantity  # remove from stock

    def remove_product(self, product, quantity=1):
        if product in self.items:
            if quantity >= self.items[product]:
                product.stock += self.items[product]  # add everything back to stock
                self.items.pop(product)  # remove product from the cart
            else: # if we aren't removing everything
                self.items[product] -= quantity  # decrease quantity in cart
                product.stock += quantity  # add back to stock
        else:
            print(f"Are you stupid? There's no {product.name} in your cart.")

    def calculate_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity  # price times amount
        return total
    
    def view_cart(self):
        if not self.items:
            print("Your cart is empty, sire.")
        else:
            print("Your cart has:")
            for product, quantity in self.items.items():
                print(f"- {product.name} x{quantity}, worth ${product.price * quantity}.")