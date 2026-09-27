inventory = 0
rejectentries = 0
deliveryentries = 0
new_value = 0

INVENTORY_FILE = "inventory.txt"
STARTING_ID = 1001


def get_valid_entries(user_input):
    if user_input.lower() == "quit":
        return "quit"
    elif user_input.isdigit() == False:
        return "error"
    else:
        return user_input


def process_delivery(current_total, added_value):
    new_value = current_total + added_value
    return new_value


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("Total units processed: " + str(total_units))
    print("Failed attempts: " + str(failed_attempts))


def load_inventory():
    
    orders = []
    total = 0

    try:
        with open(INVENTORY_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",", 2)

                # Ignore malformed lines
                if len(parts) != 3:
                    continue

                try:
                    order_id = int(parts[0].strip())
                    item_name = parts[1].strip()
                    quantity = int(parts[2].strip())
                except ValueError:
                    continue

                orders.append({
                    "id": order_id,
                    "item": item_name,
                    "quantity": quantity
                })

                total += quantity

    except FileNotFoundError:
        orders = []
        total = 0

    return orders, total


def save_inventory(orders):
    with open(INVENTORY_FILE, "w") as file:
        for order in orders:
            file.write(
                f"{order['id']},{order['item']},{order['quantity']}\n"
            )


def get_next_id(orders):
    if not orders:
        return STARTING_ID

    return max(order["id"] for order in orders) + 1


def display_orders(orders):
    print("\nCurrent Orders:")

    if not orders:
        print("No orders found.")
        return

    for order in orders:
        print(
            f"{order['id']}, {order['item']}, {order['quantity']}"
        )


orders, inventory = load_inventory()
rejectentries = 0
deliveryentries = len(orders)

display_orders(orders)

while inventory < 501:
    print("\nCurrent Inventory: " + str(inventory))

    item_name = input("Enter Product Name or quit: ")

    if item_name.lower() == "quit":
        save_inventory(orders)

        print("\nInventory successfully saved.")
        print("Total units processed: " + str(inventory))
        print("Total deliveries: " + str(deliveryentries))
        print("Total Tax: " + str(calculate_tax(inventory)))
        print("Rejected Entries: " + str(rejectentries))
        break

    if not item_name.strip():
        print("Invalid Product Name!")
        rejectentries += 1
        continue

    userinput = input("Enter Quantity: ")
    valid_entry = get_valid_entries(userinput)

    if valid_entry == "quit":
        save_inventory(orders)

        print("\nInventory successfully saved.")
        print("Total units processed: " + str(inventory))
        print("Total deliveries: " + str(deliveryentries))
        print("Total Tax: " + str(calculate_tax(inventory)))
        print("Rejected Entries: " + str(rejectentries))
        break

    if valid_entry == "error":
        print("Invalid Input!")
        rejectentries += 1
        continue

    quantity = int(valid_entry)

    if quantity <= 0:
        print("Invalid Stock!")
        rejectentries += 1
        continue

    if inventory + quantity >= 501:
        print("Stock Exceeds 500!")
        rejectentries += 1
        print("Total units processed: " + str(inventory))
        print("Total deliveries: " + str(deliveryentries))
        print("Total Tax: " + str(calculate_tax(inventory)))
        print("Rejected Entries: " + str(rejectentries))
        break

    # Generate the next order ID.
    new_id = get_next_id(orders)

    # Create the new order.
    new_order = {
        "id": new_id,
        "item": item_name.strip(),
        "quantity": quantity
    }

    # Add it to the transaction/order history.
    orders.append(new_order)

    # Update inventory.
    inventory = process_delivery(inventory, quantity)
    deliveryentries += 1

    # Append the new order to inventory.txt immediately.
    with open(INVENTORY_FILE, "a") as file:
        file.write(
            f"{new_id},{item_name.strip()},{quantity}\n"
        )

    print("\nNew Order Added:")
    print(f"{new_id},{item_name.strip()},{quantity}")
    print("Current Deliveries: " + str(deliveryentries))
    print("Current Tax: " + str(calculate_tax(inventory)))
    print("Stock Added")
