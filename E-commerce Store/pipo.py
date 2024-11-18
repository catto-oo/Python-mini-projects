class ProductManager:
    def __init__(self, products = []):
        self.products = products

    def load_products(self, filename):
        self.products.clear() # clears the list so we don't load already existing products
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
    
    # I can do this in the add_product function in the cart class
    # def update_stock(self, quantity):
    #     pass
        

class Cart:
    def __init__(self, items = {}):
        self.items = items # dict to store product names as keys and prices as values

    def add_product(self, product, quantity=1):
        if quantity > product.stock:
            print(f"Go away! We only have {product.stock} {product.name}s.")
        else:
            if product in self.items:
                self.items[product] += quantity  # add quantity to existing product
            else:
                self.items[product] = quantity  # add new product
            print(f"{quantity} {picked_product.name}(s) added to your cart.") # added later on, check line 133
            product.stock -= quantity  # remove quantity from stock

    def remove_product(self, product, quantity=1):
        if product in self.items:
            if quantity >= self.items[product]:
                product.stock += self.items.pop(product)  # remove key from dict and add its value to stock
                print(f"All {picked_product.name}s were removed from your cart.")

            else: # if we aren't removing everything
                self.items[product] -= quantity  # decrease quantity in cart
                product.stock += quantity  # add back to stock
                print(f"{quantity} {picked_product.name}(s) removed from your cart.")
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
            print("Your cart contains:")
            for i, (product, quantity) in enumerate(self.items.items()):
                print(f"{i+1}. {product.name} x{quantity}, {product.price * quantity:.2f} MAD.")


class Customer:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart
    
    def checkout(self):
        total = self.cart.calculate_total() # calculating our total
        if total == 0:
            print("Your cart is empty! Leave and never come back.")
        
        else:
            print(f"Your total is: {total:.2f} MAD.") # apparently the .2f thing makes it only have 2 decimal places
            answer = input("Would you like to proceed with the checkout? (Yes/No): ").lower()
            if answer[0] == "y":
                print(f"Your purchase is successful! Never come back {self.name}.")
                self.cart.items.clear() # clearing the cart from products
            else:
                print("9rzaz as7bi khles ola ghyerha")


laptop = Product('Laptop', 4999.99, 10)
phone = Product('Phone', 1999.99, 20)
tablet = Product("Tablet", 1499.99, 7)
mouse = Product('Mouse', 399.99, 50)
keyboard = Product('Keyboard', 599.99, 50)
gpu = Product('Ryzen 4070', 1, 1) # the memes (https://youtu.be/F1QNUKK1u_4)

prod_manager = ProductManager()
prod_manager.products = [laptop, phone, tablet, mouse, keyboard, gpu]

prod_manager.save_products(r"E-commerce Store\products.txt") # not sure what I'm doing here tbh
prod_manager.load_products(r"E-commerce Store\products.txt") # reloading the products just to make sure this doesn't go wrong

cart = Cart()
customer_name = input("Enter your name: ")
humanoid = Customer(customer_name, cart)

while True: # main loop finally
    print("\n1. View available products")
    print("2. Add product to cart")
    print("3. Remove product from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Leave")

    quickTimeEvent = input("Please type a number to access its corresponding functionality: ")

    if quickTimeEvent == "1":
        print("\n") # decoration
        print("The available products in our store are:")
        for i, product in enumerate(prod_manager.products): # the index starts at 0 so I used "i+1" to make it start at 1
            print(f"{i+1}. {product.name}, {product.price} MAD ({product.stock} left)")
    
    elif quickTimeEvent == "2":
        print("\n")
        for i, product in enumerate(prod_manager.products): # just showing the product list again
            print(f"{i+1}. {product.name}, {product.price} MAD ({product.stock} left)")

        print("\n")
        pick = int(input("Enter the number of the product which you want to add to your cart: "))
        if 1 <= pick <= len(prod_manager.products): # making sure the number is valid
            picked_product = prod_manager.products[pick - 1] # fixing the index of the product cuz yeah
            if picked_product.stock == 0:
                print("That product is out of stock.")

            else:
                amount = int(input(f"How many {picked_product.name}s would you like to have added to your cart? "))
                cart.add_product(picked_product, amount)
        else:
            print("That number isn't in the list.")

    elif quickTimeEvent == "3":
        print("\n")
        cart.view_cart()
        if cart.items: # almost same thing as adding a product
            print("\n")
            pick = int(input("Enter the number of the product which you want to remove from your cart: "))
            if 1 <= pick <= len(cart.items):
                picked_product = list(cart.items.keys())[pick - 1] # here I put the keys from the item dict into a list then get the product from it
                quantity = int(input(f"How many {picked_product.name}s would you like to remove? "))
                cart.remove_product(picked_product, quantity)
            else:
                print("That number isn't in the list.")
            
    elif quickTimeEvent == "4":
        print("\n")
        cart.view_cart()
        total = humanoid.cart.calculate_total()
        print(f"Your total is: {total:.2f} MAD.")

    elif quickTimeEvent == "5":
        print("\n")
        humanoid.checkout()
        if not cart.items:
            break # leaving the loop if the cart is empty aka the customer left

    elif quickTimeEvent == "6":
        print("\n")
        print("See you soon, or not.")
        break

    else:
        print("That number isn't in the list, try again.")