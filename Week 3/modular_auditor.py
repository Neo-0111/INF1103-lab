inventory = 0
rejectentries = 0
deliveryentries = 0
new_value = 0

def get_valid_entries(user_input):
    if user_input == "quit":
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
    print ("Total units processed: " + total_units)
    print ("Failed attempts: " + failed_attempts)

while inventory < 501:
    print ("Current Inventory: " + str(inventory))
    userinput = input("Enter inventory: ")
    get_valid_entries (userinput)
    if get_valid_entries (userinput) == "quit":
        print ("Total units processed: " + str(inventory))
        print ("Total deliveries: " + str(deliveryentries))
        print ("Total Tax: " + str(calculate_tax(inventory)))
        print ("Rejected Entries: " + str(rejectentries))
        break
    elif get_valid_entries (userinput) == "error":
        print ("Invalid Input!")
        rejectentries = rejectentries +1
        continue
    elif int(get_valid_entries (userinput)) > 0 and int(get_valid_entries (userinput)) < 501:
        if inventory < 501 and inventory + int(get_valid_entries (userinput)) < 501:
            inventory = process_delivery(inventory, int(get_valid_entries (userinput)))
            print("Current Deliveries: " + str(deliveryentries+1))
            print("Current Tax: " + str(calculate_tax(inventory)))
            print("Stock Added")
            continue
        else:
            print("Stock Exceeds 500!")
            rejectentries = rejectentries + 1
            print ("Total units processed: " + str(inventory))
            print ("Total deliveries: " + str(deliveryentries))
            print ("Total Tax: " + str(calculate_tax(inventory)))
            print ("Rejected Entries: " + str(rejectentries))
            break
    elif int(get_valid_entries (userinput)) < 0 or int(get_valid_entries (userinput)) == 0:
        print ("Invalid Stock!")
        rejectentries = rejectentries +1
        continue
    else:
        print ("Too much stock")
        rejectentries = rejectentries +1
        continue
    
