class Customer:
    def __init__(self, first_name: str, last_name: str):
        # default values to be updated
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = 0

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}"

    def __dict__(self):
        return dict(first_name=self.first_name, last_name=self.last_name, customer_id=self.customer_id)
