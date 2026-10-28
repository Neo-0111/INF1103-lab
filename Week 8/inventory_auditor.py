import json
import os

from inventory import Inventory
from product import Product


# ==========================================
# INVENTORY MANAGEMENT SYSTEM (OOP VERSION)
# ==========================================

FILE_NAME = "inventory.json"


# ==========================================
# FILE HANDLING
# ==========================================

def create_default_inventory():
    """Create an Inventory containing the default products."""
    inventory = Inventory()
    inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
    inventory.add_product(Product("P002", "Mouse", 25.50, 40))
    inventory.add_product(Product("P003", "Keyboard", 45.00, 25))
    return inventory


def load_inventory():
    #Load inventory from inventory.json and return an Inventory object
    #If the file is missing or unreadable, use the default inventory
    
    if not os.path.exists(FILE_NAME):
        print("inventory.json not found.")
        print("Starting with default inventory.\n")
        return create_default_inventory()

    print("inventory.json found.")

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        # New format is {"inventory": [...]}; older format was a plain list
        if isinstance(data, dict):
            product_dicts = data.get("inventory", [])
        else:
            product_dicts = data

        inventory = Inventory()
        for product_dict in product_dicts:
            inventory.add_product(Product.from_dict(product_dict))

        print("Inventory loaded successfully.")
        return inventory

    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        print("Error reading inventory.json.")
        print("Starting with default inventory.\n")
        return create_default_inventory()


def save_inventory(inventory):
    #Save the Inventory object's products to inventory.json
    data = {
        "inventory": [product.to_dict() for product in inventory.get_products()]
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# ==========================================
# USER INPUT HELPERS
# ==========================================

def prompt_non_empty(message):
    #Keep asking until the user enters something non-empty
    while True:
        value = input(message).strip()
        if value != "":
            return value
        print("This field cannot be empty.")


def prompt_price():
    #Keep asking until the user enters a valid non-negative price
    while True:
        try:
            price = float(input("Price: "))
            if price < 0:
                print("Price cannot be negative.")
            else:
                return price
        except ValueError:
            print("Please enter a valid number.")


def prompt_stock(message="Stock Quantity: "):
    #Keep asking until the user enters a valid non-negative whole number
    while True:
        try:
            stock = int(input(message))
            if stock < 0:
                print("Stock cannot be negative.")
            else:
                return stock
        except ValueError:
            print("Please enter a whole number.")


# ==========================================
# MENU ACTIONS (they call Inventory methods)
# ==========================================

def add_product_menu(inventory):
    print("\nAdd New Product")

    # Ask for the ID first so a duplicate is caught before other questions
    while True:
        product_id = prompt_non_empty("Product ID: ").upper()

        if inventory.search_product(product_id) is None:
            break

        print("Product ID already exists. Please enter another ID.")

    name = prompt_non_empty("Product Name: ")
    price = prompt_price()
    stock = prompt_stock()

    product = Product(product_id, name, price, stock)
    inventory.add_product(product)

    print("\nProduct added successfully!")


def update_stock_menu(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product.name}")
    print(f"Current Stock: {product.stock}")

    new_stock = prompt_stock("\nNew Stock Quantity: ")
    product.update_stock(new_stock)

    print("\nStock updated successfully!")


def search_product_menu(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-" * 40)
    product.display_information()
    print("-" * 40)


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    inventory = load_inventory()

    while True:
        print("\nMENU")
        print("--------------------------------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------------------")

        choice = input("\nEnter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product_menu(inventory)

        elif choice == "3":
            update_stock_menu(inventory)

        elif choice == "4":
            search_product_menu(inventory)

        elif choice == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)

        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("\nInvalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
