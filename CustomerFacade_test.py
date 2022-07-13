import pytest
from FacadeBase import FacadeBase
from AdministratorFacade import AdministratorFacade
from AirlineCompanyFacade import AirlineCompanyFacade
from AnonymousFacade import AnonymousFacade
from Customer import Customer
from CustomerFacade import CustomerFacade
from DbRepo import DbRepo
from Exceptions import CustomerDoesNotExist, NegativeDataError, FlightDoesNotExistException, \
    TicketDoesNotExist
from Flights import Flights
from Ticket import Ticket
from db2_config import local_session2
from db2_config import config

repo = DbRepo(local_session2)

@pytest.fixture(scope='session')
def customer_facade_object():
    anonymous_facade = AnonymousFacade(DbRepo, config)
    return anonymous_facade.login('roy','Aa123456!')


@pytest.fixture(scope='function', autouse=True)
def reset_db(customer_facade_object):
    customer_facade_object.repo.reset_test_db()

def update_customer_success_test(customer_facade_object):
    customer = Customer(first_name= 'roy', last_name= 'duvdev', address= 'tel aviv', phone_no= 235,
                credit_card_no= 152, user_id= 76)
    customer_facade_object.add_customer(customer)
    customer2 = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                 credit_card_no= 1521, user_id= 76)
    customer2_name = 'roy1'
    customer_facade_object.update_customer(customer2)
    update_customer = repo.get_by_name(Customer, customer2_name)
    assert customer2 in update_customer == True


def update_customer_not_exist_test(customer_facade_object):
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 76)
    with pytest.raises(CustomerDoesNotExist):
        customer_facade_object.update_customer(customer)


def update_customer_negative_user_id_test(customer_facade_object):
    customer1 = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= -1)
    with pytest.raises(NegativeDataError):
        customer_facade_object.update_customer(customer1)


def add_ticket_success_test(customer_facade_object):
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 76)
    flight = Flights(airline_company_id= 6, origin_country_id= 'israel', destination_country_id= 6, departure_time= 5,
              landing_time= 7, remaining_tickets= 6)
    ticket = Ticket(flight_id= 5, customer_id = 2)
    customer_facade_object.add_customer(customer)
    customer_facade_object.add_flight(flight)
    customer_facade_object.add_ticket(ticket)
    tickets = customer_facade_object.get_tickets_by_customer(customer)
    assert ticket in tickets == True


def add_ticket_flightNotExist_test(customer_facade_object):
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address='tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 76)
    ticket = {'flight_id': 5, 'customer_id': 2}
    customer_facade_object.add_customer(customer)
    with pytest.raises(FlightDoesNotExistException):
        customer_facade_object.add_ticket(ticket)


def add_ticket_negative_customer_Id_test(customer_facade_object):
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= -1)
    flight = Flights(airline_company_id= 6,origin_country_id= 'israel', destination_country_id= 6, departure_time= 5,
              landing_time= 7, remaining_tickets= 6)
    ticket = Ticket(flight_id= 5, customer_id= -1)
    customer_facade_object.add_customer(customer)
    customer_facade_object.add_flight(flight)
    with pytest.raises(NegativeDataError):
        customer_facade_object.add_ticket(ticket)


def add_ticket_negative_flight_id_test(customer_facade_object):
    customer = Customer(first_name='roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 2)
    flight = Flights (airline_company_id= 6, origin_country_id= 'israel', destination_country_id= 6, departure_time= 5,
              landing_time= 7, remaining_tickets= 6)
    ticket = Ticket(flight_id= -1, customer_id= 2)
    customer_facade_object.add_customer(customer)
    customer_facade_object.add_flight(flight)
    with pytest.raises(NegativeDataError):
        customer_facade_object.add_ticket(ticket)


def remove_ticket_success_test(customer_facade_object):
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 2)
    flight =Flights (airline_company_id= 6, origin_country_id= 'israel', destination_country_id= 6, departure_time= 5,
              landing_time= 7, remaining_tickets= 6)
    ticket =Ticket (flight_id= 1, customer_id= 2)
    customer_facade_object.add_customer(customer)
    customer_facade_object.add_flight(flight)
    customer_facade_object.add_ticket(ticket)
    customer_facade_object.remove_ticket(ticket)
    tickets = customer_facade_object.get_tickets_by_customer(customer)
    assert ticket in tickets == False


def remove_ticket_negative_customer_id_test(customer_facade_object):
    customer =Customer (first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= -1)
    flight = Flights(airline_company_id= 6,origin_country_id= 'israel', destination_country_id= 6, departure_time= 5,
              landing_time= 7, remaining_tickets= 6)
    ticket = {'flight_id': 1, 'customer_id': -1}
    customer_facade_object.add_customer(customer)
    customer_facade_object.add_flight(flight)
    customer_facade_object.add_ticket(ticket)
    with pytest.raises(NegativeDataError):
        customer_facade_object.remove_ticket(ticket)


def remove_ticket_negative_flight_id_test(customer_facade_object):
    customer =Customer (first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521,user_id= 1)
    flight = Flights(airline_company_id= 6, origin_country_id= 'israel', destination_country_id= 6, departure_time= 5,
              landing_time= 7, remaining_tickets= 6)
    ticket =Ticket (flight_id= -1, customer_id= 1)
    customer_facade_object.add_customer(customer)
    customer_facade_object.add_flight(flight)
    customer_facade_object.add_ticket(ticket)
    with pytest.raises(NegativeDataError):
        customer_facade_object.remove_ticket(ticket)


def remove_ticket_DoesNotExist_test(customer_facade_object):
    ticket = Ticket(flight_id= -1, customer_id= 1)
    with pytest.raises(TicketDoesNotExist):
        customer_facade_object.remove_ticket(ticket)
        customer_facade_object.remove_ticket(ticket)
