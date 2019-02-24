"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    customer_list = {}

    def __init__(self,first,last,email,password):

        self.first = first
        self.last = last
        self.email = email
        self.password = password


    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return ("<Customer: {}, {}, {}>".format(self.first, 
            self.last, self.email))


    def read_customer(filepath):

        customers = {}

        file = open(filepath)

        for line in file:
            customer = line.rstrip().split('|')
            fis



    customer_list = read_customer('customer.txt')