class Inventory:
    
    #Manages a collection of Product objects

    #Responsibility (SRP): store, add, search and display products
    #It does not ask the user for input or read/write files
    

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        
        #Add a Product to the inventory.
        #Returns True if added, False if the product ID already exists.
        
        if self.search_product(product.product_id) is not None:
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id):
        #Return the Product with the given ID, or None if not found
        product_id = product_id.strip().upper()

        for product in self.__products:
            if product.product_id == product_id:
                return product

        return None

    def display_all(self):
        #Display every product in the inventory
        print("\nCurrent Inventory")
        print("-" * 40)

        if len(self.__products) == 0:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()

        print("-" * 40)

    def get_products(self):
        #Return a copy of the product list (so callers can't alter ours).
        return list(self.__products)
