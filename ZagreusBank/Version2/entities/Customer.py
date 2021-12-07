class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str):
        # default values to be updated
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}"

    def create_customer_dictionary(self):
        return dict(customer_id=self.customer_id, first_name=self.first_name, last_name=self.last_name)
