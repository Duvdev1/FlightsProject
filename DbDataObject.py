import json

from RabbitProducerObject import RabbitProducerObject
import LoaderToApp


class DbDataObject:
    def __init__(self, customers, airlines, flights_per_company, tickets_per_customer):
        self.customers = customers
        self.airlines = airlines
        self.flights_per_company = flights_per_company
        self.tickets_per_customer = tickets_per_customer
        self.rabbit_producer = RabbitProducerObject('GenerateData')
        self.loader = LoaderToApp

    def validate(self):
        if self.customers < 0 or self.airlines < 0 or self.flights_per_company < 0 or \
                self.tickets_per_customer < 0:
            print("g")
            return False
        print("r")
        #DbDataObject.Generate_Data(self, db_data)
        return True

    def Generate_Data(self):
        self.loader.db_reset()
        self.loader.generate_user_role()
        self.loader.country_loader()
        self.loader.customer_loader(self.customers)
        self.loader.administrator_loader(self.administrators)
        self.loader.airline_loader(self.airlines)
        self.loader.flights_loader(self.flights_per_company)
        self.loader.tickets_loader(self.tickets_per_customer)


    def __str__(self):
        return f'{{"customers": {self.customers},' \
               f' "administrators": {self.administrators}, ' \
               f'"airlines": {self.airlines} , "flights_per_company": {self.flights_per_company}, ' \
               f'"tickets_per_customer":{self.tickets_per_customer}}}'

    def __dict__(self):
        return {'customers': self.customers,
                 'administrators': self.administrators,
                 'airlines': self.airlines, 'flights_per_company': self.flights_per_company,
                 'tickets_per_customer': self.tickets_per_customer}
