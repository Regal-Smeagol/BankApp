class Customer:
    """Class Variables"""
    total_active_customers = 0
    customers_on_record = 0

    def __init__(self, first_name: str, last_name: str):
        # default values to be updated
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = 0

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
