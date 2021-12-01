from abc import ABC  # Remove this later


class Account(ABC):

    def __init__(self):
        pass

    def __str__(self):
        return "first name: {}, last name: {}, jersey number: {}, player ID: {}, team ID: {}".format(self.first_name, self.last_name, self.cust)