class Customer:
    def __init__(self, customer_data):
        self.first_name = customer_data["first_name"]
        self.last_name = customer_data["last_name"]
        self.customer_id = customer_data["customer_id"]

    def get_customer_as_dictionary(self):
        return dict(first_name=self.first_name, last_name=self.last_name, customer_id=self.customer_id)
