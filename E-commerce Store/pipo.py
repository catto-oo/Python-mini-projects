class ProductManager:
    def __init__(self, products):
        self.products = products

    def load_products(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                price = float(data[1])
                stock = int(data[2])

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