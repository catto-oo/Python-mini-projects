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
    def __init__(self, items = []):
        self.items = items
    
    def add_product(self, product, quantity = 1):
        # checks if we have the amount that the client wants
        if quantity > product.stock:
            print(f"Go away! We only have {product.stock} of {product.name}.")

        else: # adds the product to the item list and removes it from stock
            for i in range(quantity):
                self.items.append(product)
                product.stock -= 1

    def remove_product(self, product):
        # idk how to implement removing more than 1 of the same product so I just won't lmao
        self.items.pop(product)
        product.stock += 1

    def calculate_total():
        pass