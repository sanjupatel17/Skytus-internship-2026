#simple cart managment system

class Cart:
    def __init__(self):
        self.items = {}  

    def add_item(self, item, quantity, price):
        if item in self.items:
            self.items[item][0] += quantity
        else:
            self.items[item] = [quantity, price]
        print(f" {item} added to cart")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"🗑 {item} removed from cart")
        else:
            print(" Item not found in cart")

    def view_cart(self):
        if not self.items:
            print(" Cart is empty")
            return

        print("\n Cart Details")
        total = 0
        for item, data in self.items.items():
            qty, price = data
            cost = qty * price
            total += cost
            print(f"{item} x {qty} = ₹{cost}")

        print(f"Total Amount: ₹{total}")


# -------- Main Program --------
print("Welcome to the Cart Management System")

cart = Cart()

while True:
    print("\nChoose an option:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: ₹"))
        cart.add_item(item, quantity, price)

    elif choice == '2':
        item = input("Enter item name to remove: ")
        cart.remove_item(item)

    elif choice == '3':
        cart.view_cart()

    elif choice == '4':
        print("Thank you for using the Cart Management System")
        break

    else:
        print("Invalid choice. Please try again.")





