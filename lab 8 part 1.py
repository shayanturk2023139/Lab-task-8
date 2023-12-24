                                                                                                                                                                                            
    def _init_(self, name, price):
        self.name = name
        self.price = price

    def _str_(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_to_cart(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product} x{quantity}")

    def calculate_total(self):
        total_cost = sum(item["product"].price * item["quantity"] for item in self.items)
        return total_cost


class Customer:
    def _init_(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_to_cart(product, quantity)

    def display_cart(self):
        self.shopping_cart.display_cart()

    def checkout(self):
        total_cost = self.shopping_cart.calculate_total()
        print(f"\nTotal cost: ${total_cost:.2f}")
        print("Thank you for shopping with us!")


# Example usage:
if _name_ == "_main_":
    product1 = Product("Laptop", 1200.50)
    product2 = Product("Headphones", 99.99)
    product3 = Product("Mouse", 19.95)

    customer = Customer("Alice")

    customer.add_to_cart(product1, 2)
    customer.add_to_cart(product2)
    customer.add_to_cart(product3, 3)

    customer.display_cart()

    customer.checkout()
                                                                                                                                                                                           from datetime import datetime

