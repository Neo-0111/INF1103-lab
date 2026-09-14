inventory = 0
rejectentries = 0

while inventory < 501:
    print ("Current Inventory: " + str(inventory))
    userinput = input("Enter inventory: ")
    if userinput == "quit":
            print ("Total units processed: " + str(inventory))
            print ("Rejected Entries: " + str(rejectentries))
            break
    elif userinput.isdigit() == False:
        print ("Invalid Input!")
        rejectentries = rejectentries +1
        continue
    elif int(userinput) > 0 and int(userinput) < 501:
            if inventory < 501 and inventory + int(userinput) < 501:
                 inventory = inventory + int(userinput)
                 print("Stock Added")
                 continue
            else:
                print("Stock Exceeds 500!")
                print ("Total units processed: " + str(inventory))
                print ("Rejected Entries: " + str(rejectentries))
                 break
    elif int(userinput) < 0 or int(userinput) == 0:
        print ("Invalid Stock!")
        rejectentries = rejectentries +1
        continue
    else:
        print ("Too much stock")
        rejectentries = rejectentries +1
        continue
