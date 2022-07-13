from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from sqlalchemy import false
from DbDataObject import DbDataObject
from RabbitConsumerObject import RabbitConsumerObject
from RabbitProducerObject import RabbitProducerObject
from LoggingApp import LoggingApp
from DbRepo import DbRepo
from db_config import local_session
import json


class DbGenWidget(Widget):
    airline_companies = ObjectProperty(None)
    customers = ObjectProperty(None)
    administrators = ObjectProperty(None)
    flights_per_company = ObjectProperty(None)
    tickets_per_customer = ObjectProperty(None)
    countries = ObjectProperty(None)
    rabbit_producer = RabbitProducerObject('DataToGenerate')
    alerts_label = StringProperty('')
    dbrepo = DbRepo(local_session)
    already_generated = false

    # root.btn() in kv file
    def btn(self):
        if self.already_generated:
            self.ids.alerts_label.text = "All data has been generate!"
            return
        
        airlinescom = self.airline_companies.text
        customers = self.customers.text
        countries = self.countries.text
        flights = self.flights_per_company.text
        tickets = self.tickets_per_customer.text
        db_data = DbDataObject(customers=customers, airlines=airlinescom, 
                               flights_per_company=flights, 
                               tickets_per_customer=tickets)
        db_data.validate()
        self.rabbit_producer.publish(json.dumps(db_data.__dict__()))
        self.ids.alerts_label.text = "generating data"
        
        print("Airline Companies:", self.airline_companies.text,
              "Customers:", self.customers.text,
              "Administrators:", self.administrators.text,
              "Flights Per Company:", self.flights_per_company.text,
              "Tickets Per Customer:", self.tickets_per_customer.text)

    



Builder.load_file('MyApp.kv')

if __name__ == "__main__":
    MyApp().run()