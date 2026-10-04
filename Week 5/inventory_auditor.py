import json
import os


# ==========================================
# INVENTORY MANAGEMENT SYSTEM
# ==========================================

FILE_NAME = "inventory.json"


# ==========================================
# DEFAULT INVENTORY
# ==========================================

default_inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]


# ==========================================
# LOAD INVENTORY
# ==========================================

def load_inventory():
    """
    Load inventory from inventory.json.
    If the file does not exist, use the default inventory.
    """

    if os.path.exists(FILE_NAME):
        print("inventory.json found.")

        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            # Support inventory + transaction history
            if isinstance(data, dict):
                inventory = data.get("inventory", [])
                transaction_history = data.get("transaction_history", [])
            else:
                # If an older JSON contains only a list
                inventory = data
                transaction_history = []

            print("Inventory loaded successfully.")
            return inventory, transaction_history

        except json.JSONDecodeError:
            print("Error reading inventory.json.")
            print("Starting with default inventory.\n")

    else:
        print("inventory.json not found.")
        print("Starting with default inventory.\n")

    return default_inventory.copy(), []


# ==========================================
# SAVE INVENTORY
# ==========================================

def save_inventory(inventory, transaction_history):
    """
    Save inventory and transaction history to inventory.json.
    """

    data = {
        "inventory": inventory,
        "transaction_history": transaction_history
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# ==========================================
# DISPLAY ALL PRODUCTS
# ==========================================

def display_all(inventory):
    """
    Display all products in the inventory.
    """

    print("\nCurrent Inventory")
    print("-" * 40)

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("-" * 40)


# ==========================================
# ADD PRODUCT
# ==========================================

def add_product(inventory, transaction_history):
    """
    Add a new product to the inventory.
    """

    print("\nAdd New Product")

    # Product ID
    while True:
        product_id = input("Product ID: ").strip().upper()

        if product_id == "":
            print("Product ID cannot be empty.")
            continue

        # Check duplicate ID
        duplicate = False

        for product in inventory:
            if product["id"] == product_id:
                duplicate = True
                break

        if duplicate:
            print("Product ID already exists. Please enter another ID.")
        else:
            break

    # Product name
    while True:
        name = input("Product Name: ").strip()

        if name == "":
            print("Product name cannot be empty.")
        else:
            break

    # Price validation
    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Stock validation
    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    # Create product dictionary
    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    # Store transaction history
    transaction_history.append({
        "type": "ADD",
        "product_id": product_id,
        "amount": stock
    })

    print("\nProduct added successfully!")


# ==========================================
# UPDATE STOCK
# ==========================================

def update_stock(inventory, transaction_history):
    """
    Update the stock quantity of an existing product.
    """

    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()

    found_product = None

    for product in inventory:
        if product["id"] == product_id:
            found_product = product
            break

    if found_product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {found_product['name']}")
    print(f"Current Stock: {found_product['stock']}")

    # New stock validation
    while True:
        try:
            new_stock = int(input("\nNew Stock Quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    # Calculate transaction amount
    difference = new_stock - found_product["stock"]

    # Update stock
    found_product["stock"] = new_stock

    # Save transaction
    transaction_history.append({
        "type": "UPDATE_STOCK",
        "product_id": product_id,
        "amount": difference
    })

    print("\nStock updated successfully!")


# ==========================================
# SEARCH PRODUCT
# ==========================================

def search_product(inventory):
    """
    Search for a product using its ID.
    """

    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()

    found_product = None

    for product in inventory:
        if product["id"] == product_id:
            found_product = product
            break

    if found_product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-" * 40)
    print(f"ID: {found_product['id']}")
    print(f"Name: {found_product['name']}")
    print(f"Price: ${found_product['price']:.2f}")
    print(f"Stock: {found_product['stock']}")
    print("-" * 40)


# ==========================================
# DISPLAY TRANSACTION HISTORY
# ==========================================

def display_transaction_history(transaction_history):
    """
    Display all recorded stock transactions.
    """

    print("\nTransaction History")
    print("-" * 40)

    if len(transaction_history) == 0:
        print("No transactions recorded.")
    else:
        for transaction in transaction_history:
            print(
                f"Type: {transaction['type']} | "
                f"Product ID: {transaction['product_id']} | "
                f"Amount: {transaction['amount']}"
            )

    print("-" * 40)


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    # Load existing inventory
    inventory, transaction_history = load_inventory()

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

        # ==================================
        # OPTION 1 - DISPLAY
        # ==================================

        if choice == "1":
            display_all(inventory)

        # ==================================
        # OPTION 2 - ADD
        # ==================================

        elif choice == "2":
            add_product(inventory, transaction_history)

        # ==================================
        # OPTION 3 - UPDATE
        # ==================================

        elif choice == "3":
            update_stock(inventory, transaction_history)

        # ==================================
        # OPTION 4 - SEARCH
        # ==================================

        elif choice == "4":
            search_product(inventory)

        # ==================================
        # OPTION 5 - SAVE
        # ==================================

        elif choice == "5":
            print("\nSaving inventory...")
            save_inventory(inventory, transaction_history)

        # ==================================
        # OPTION 6 - EXIT
        # ==================================

        elif choice == "6":

            print("\nSaving inventory before exit...")
            save_inventory(inventory, transaction_history)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")

            break

        # ==================================
        # INVALID OPTION
        # ==================================

        else:
            print("\nInvalid option. Please enter a number from 1 to 6.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()