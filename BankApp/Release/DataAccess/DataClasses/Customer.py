class Customer:
    def __init__(self, first_name: str, last_name: str, customer_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id

    def get_customer_as_dictionary(self):
        return dict(first_name=self.first_name, last_name=self.last_name, customer_id=self.customer_id)
