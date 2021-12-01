class Customer:
    """Class Variables"""
    total_active_customers = 0
    customers_on_record = 0

    def __init__(self, customer_data: dict):
        if customer_data is None:
            customer_data = dict(first_name="N/A", last_name="N/A", customer_id="N/A")

        self.first_name = customer_data["first_name"]
        self.last_name = customer_data["last_name"]
        self.customer_id = customer_data["customer_id"]

    def get_customer_as_dictionary(self):
        return dict(first_name=self.first_name, last_name=self.last_name, customer_id=self.customer_id)

    @classmethod
    def increment_customers_on_record(cls):
        cls.customers_on_record += 1

    @classmethod
    def increment_active_customers(cls):
        cls.total_active_customers += 1

    @classmethod
    def decrement_customers_on_record(cls):
        cls.customers_on_record -= 1

    @classmethod
    def decrement_active_customers(cls):
        cls.total_active_customers -= 1

    @classmethod
    def customer_id_generator(cls) -> int:
        return int(cls.customers_on_record * 13/7)
