#
from abc import ABC, abstractmethod



# 1. ABSTRACT CLASS


class Food(ABC):

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    @abstractmethod
    def calculate_price(self, quantity):
        pass



# 2. CHILD CLASSES


class Momo(Food):

    def calculate_price(self, quantity):
        return self.get_price() * quantity


class Pizza(Food):

    def calculate_price(self, quantity):
        return self.get_price() * quantity


class Burger(Food):

    def calculate_price(self, quantity):
        return self.get_price() * quantity


class Chowmein(Food):

    def calculate_price(self, quantity):
        return self.get_price() * quantity


# 3. FOOD MENU


foods = [
    Momo("Momo", 150),
    Pizza("Pizza", 350),
    Burger("Burger", 200),
    Chowmein("Chowmein", 180)
]


# 4. ORDER MANAGEMENT CLASS

class Order:

    def __init__(self):
        self.cart = {}

    # Display menu
    def show_menu(self):

        print("\n========== FOOD MENU ==========")

        for index, food in enumerate(foods, start=1):
            print(
                f"{index}. {food.name:<12} Rs. {food.get_price()}"
            )

        print("================================")

    # Add food to cart
    def add_item(self):

        self.show_menu()

        try:
            choice = int(input("Enter food number: "))

            if choice < 1 or choice > len(foods):
                print("Invalid food selection!")
                return

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero!")
                return

            food = foods[choice - 1]
            name = food.name

            if name in self.cart:
                self.cart[name]["quantity"] += quantity
            else:
                self.cart[name] = {
                    "food": food,
                    "quantity": quantity
                }

            print(f"{quantity} {name} added successfully!")

        except ValueError:
            print("Please enter a valid number!")

    # View cart
    def view_cart(self):

        if not self.cart:
            print("\nYour cart is empty!")
            return

        print("\n========== YOUR CART ==========")

        for name, item in self.cart.items():

            food = item["food"]
            quantity = item["quantity"]

            total = food.calculate_price(quantity)

            print(
                f"{name:<12} x {quantity:<3} = Rs. {total}"
            )

        print("================================")

    # Remove item
    def remove_item(self):

        if not self.cart:
            print("\nYour cart is empty!")
            return

        self.view_cart()

        name = input("\nEnter food name to remove: ").strip().title()

        if name in self.cart:
            del self.cart[name]
            print(f"{name} removed successfully!")
        else:
            print("Food item not found in cart!")

    # Update quantity
    def update_quantity(self):

        if not self.cart:
            print("\nYour cart is empty!")
            return

        self.view_cart()

        name = input("\nEnter food name to update: ").strip().title()

        if name not in self.cart:
            print("Food item not found!")
            return

        try:
            quantity = int(input("Enter new quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero!")
                return

            self.cart[name]["quantity"] = quantity

            print("Quantity updated successfully!")

        except ValueError:
            print("Please enter a valid number!")

    # Calculate subtotal
    def calculate_subtotal(self):

        subtotal = 0

        for item in self.cart.values():

            food = item["food"]
            quantity = item["quantity"]

            subtotal += food.calculate_price(quantity)

        return subtotal

    # Calculate discount
    def calculate_discount(self):

        subtotal = self.calculate_subtotal()

        if subtotal > 1000:
            return subtotal * 0.10

        return 0

    # Generate receipt
    def generate_receipt(self):

        if not self.cart:
            print("\nCannot generate receipt. Cart is empty!")
            return

        print("\n")
        print("========== FINAL RECEIPT ==========")

        for name, item in self.cart.items():

            food = item["food"]
            quantity = item["quantity"]

            total = food.calculate_price(quantity)

            print(
                f"{name:<12} x {quantity:<3} = Rs. {total:.2f}"
            )

        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        final_amount = subtotal - discount

        print("-----------------------------------")
        print(f"Subtotal:       Rs. {subtotal:.2f}")
        print(f"Discount (10%): Rs. {discount:.2f}")
        print("-----------------------------------")
        print(f"Final Amount:   Rs. {final_amount:.2f}")
        print("===================================")
        print("       THANK YOU FOR ORDERING!")
        print("===================================")

        self.cart.clear()



# 5. MAIN PROGRAM


def main():

    order = Order()

    while True:

        print("\n========== FOOD ORDERING SYSTEM ==========")
        print("1. Show Food Menu")
        print("2. Add Food to Cart")
        print("3. View Cart")
        print("4. Update Quantity")
        print("5. Remove Food")
        print("6. Generate Receipt")
        print("7. Exit")
        print("==========================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                order.show_menu()

            elif choice == 2:
                order.add_item()

            elif choice == 3:
                order.view_cart()

            elif choice == 4:
                order.update_quantity()

            elif choice == 5:
                order.remove_item()

            elif choice == 6:
                order.generate_receipt()

            elif choice == 7:
                print("Thank you! Visit again.")
                break

            else:
                print("Invalid choice! Select 1-7.")

        except ValueError:
            print("Please enter a valid number!")


# Run the program
if __name__ == "__main__":
    main()
