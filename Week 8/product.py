class Product:
    
    #Represents and manages a single product

    #Responsibility (SRP): store product information and manage its own state
    #It does not load/save files, ask for input, or manage a collection
    

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = 0

        # Route the initial stock through update_stock so validation is shared
        self.update_stock(stock)

    # ------------------------------------------------------------------
    # Read-only access to private attributes
    # ------------------------------------------------------------------

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    # ------------------------------------------------------------------
    # Behaviour
    # ------------------------------------------------------------------

    def update_stock(self, quantity):
        
        #Set the stock to a new quantity
        #The Product decides what is valid: stock must be a non-negative integer
        
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")

        self.__stock = quantity

    def display_information(self):
        #Print this product's details on one line
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    # ------------------------------------------------------------------
    # Conversion helpers (used by the file handling code)
    # ------------------------------------------------------------------

    def to_dict(self):
        #Return the product as a dictionary suitable for JSON
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    @classmethod
    def from_dict(cls, data):
        #Create a Product from a dictionary loaded from JSON
        return cls(data["id"], data["name"], data["price"], data["stock"])
