class Supermarket:
    def __init__(self):  #Initialize supermarket inventory with product, price per item and available quantity
        self.inventory = {     #Invetory is to define a list of product with its price and quantity
            "Apple": {"price": 2, "quantity": 50},
            "Banana": {"price": 5, "quantity": 35},
            "Milk": {"price": 4, "quantity": 40},
            "Bread": {"price": 2.5, "quantity": 15},
            "Oil": {"price": 1.8, "quantity": 25},
            "Towels": {"price":8, "quantity": 45},
            "Rice": {"price":7.5, "quantity":60}
        }

    def display_inventory(self): #To display inventory.
        print("Available items in the supermarket: ")
        for product, details in self.inventory.items():
            print(f"{product}: ${details['price']} (Quantity: {details['quantity']})")

    def check_stock(self, product, quantity): #To check if there is available items in supermarket
        if self.inventory.get(product, None) and self.inventory[product]['quantity'] >= quantity:
            return True
        else:
            return False

    def update_inventory(self, product, quantity): #Update inventory after a purchase
        if product in self.inventory:
            self.inventory[product]['quantity'] -= quantity

    def generate_receipt(self, cart):  #Generate and print a receipt for the customer
        total = 0
        receipt = "Receipt:\n"
        for product, quantity in cart.items():
            if self.check_stock(product, quantity):
                price = self.inventory[product]['price']
                total += price * quantity
                receipt += f"{product} x {quantity} = ${price * quantity:.2f}\n"
                self.update_inventory(product, quantity)
            else:
                receipt += f"Sorry, not enough stock for {product}.\n"
        receipt += f"Total: ${total:.2f}\n"
        print(receipt)

    def process_customer(self):  #Allow customer to shop and fill their cart
        cart = {}
        self.display_inventory()

        while True:
            product = input("Enter a product to add to your cart (or 'done' to finish): ").capitalize()
            if product == 'Done':
                break
            if product not in self.inventory:
                print(f"Sorry, we don't have {product}. Please choose a valid product.")
                continue
            quantity = int(input(f"Enter quantity for {product}: "))
            if self.check_stock(product, quantity):
                cart[product] = quantity
            else:
                print(f"Sorry, we only have {self.inventory[product]['quantity']} of {product} available.")
        # Generate the receipt after cart is filled
        self.generate_receipt(cart)

# Create supermarket instance
supermarket = Supermarket()

# Simulate shopping for a customer
supermarket.process_customer()

# Simulate another customer
print("\nNext Customer:\n")
supermarket.process_customer()