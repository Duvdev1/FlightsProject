import pytest
from AdministratorFacade import AdministratorFacade
from AirlineCompany import AirlineCompany
from AirlineCompanyFacade import AirlineCompanyFacade
from AnonymousFacade import AnonymousFacade
from CustomerFacade import CustomerFacade
from DbRepo import DbRepo
from Exceptions import NegativeDataError, FlightDoesNotExistException, AirlineDoesNotExist
from FacadeBase import FacadeBase
from Flights import Flights
from db_config import config
from db2_config import local_session2
from User import User

repo = DbRepo(local_session2)

@pytest.fixture(scope='sessiom=n')
def airlinecompany_facade_object():
    anonymous_facade = AnonymousFacade(DbRepo, config)
    return anonymous_facade.login('roy','Aa123456!')

@pytest.fixture(scope='function',autouse=True)
def reset_db(airlinecompany_facade_object):
    airlinecompany_facade_object.repo.reset_test_db()

def update_airline_success_test(airlinecompany_facade_object):
    user = User(user_name= 'roy', password= 655, email= 'duv', user_role= 6)
    airline = AirlineCompany(name= 'el al',country_id= 8, user_id= 7)
    airline_name = 'el al'
    airlinecompany_facade_object.add_customer(user)
    airlinecompany_facade_object.add_airline(airline)
    id = repo.get_by_name(AirlineCompany, airline_name)
    airline2 = AirlineCompany(id= id.id, name= 'el al', country_id= 6, user_id= 1)
    airlinecompany_facade_object.update_airline(airline2)
    check_airline = repo.get_by_id(AirlineCompany, airline2.id)
    assert airline2 == check_airline


def update_airline_DoesNotExist_test(airlinecompany_facade_object):
    airline = AirlineCompany(name= 'el al',country_id= 8, user_id= 7)
    airlinecompany_facade_object.remove_airline(airline)
    with pytest.raises(AirlineDoesNotExist):
        airlinecompany_facade_object.update_airline(airline)
        airlinecompany_facade_object.update_airline(airline)


def update_airline_negative_country_id_test(airlinecompany_facade_object):
    airline1 =AirlineCompany(name= 'el al',country_id= 8, user_id= 7)
    airlinecompany_facade_object.add_airline(airline1)
    airline = AirlineCompany(name= 'el al',country_id= -8, user_id= 7)
    with pytest.raises(NegativeDataError):
        airlinecompany_facade_object.update_airline(airline)
        airlinecompany_facade_object.update_airline(airline)


def update_airline_negative_user_id_test(airlinecompany_facade_object):
    airline1 =AirlineCompany(name= 'el al',country_id= 8, user_id= 7)
    airlinecompany_facade_object.add_airline(airline1)
    airline = AirlineCompany(name= 'el al',country_id= 8, user_id= -7)
    with pytest.raises(NegativeDataError):
        airlinecompany_facade_object.update_airline(airline)
        airlinecompany_facade_object.update_airline(airline)


def update_flight_success_test(airlinecompany_facade_object):
    user = User(user_name= 'roy', password = 655, email= 'duv', user_role= 6)
    airline = AirlineCompany(name= 'el al',country_id= 6, user_id= -6)
    flight = Flights(id= 1,airline_company_id= 6, origin_country_id= 5, destination_country_id= 5,
              departure_time= 7, landing_time= 3, remaining_tickets= 9)
    airlinecompany_facade_object.add_customer(user)
    airlinecompany_facade_object.add_airline(airline)
    airlinecompany_facade_object.add_flight(flight)
    flight2 = Flights(id= 1, airline_company_id= 3, origin_country_id= 5, destination_country_id= 5,
               departure_time= 7, landing_time= 6, remaining_tickets= 9)
    flight2_id = 1
    airlinecompany_facade_object.update_flight(flight2)
    check_flight = repo.get_by_id(Flights, flight2_id)
    assert flight2 == check_flight


def update_flight_DoesNotExist_test(airlinecompany_facade_object):
    flight = Flights(airline_company_id= 6, origin_country_id= 5, destination_country_id= 5,
              departure_time= 7, landing_time= 3, remaining_tickets= 9)
    airlinecompany_facade_object.remove_flight(flight)
    with pytest.raises(FlightDoesNotExistException):
        airlinecompany_facade_object.update_flight(flight)
        airlinecompany_facade_object.update_flight(flight)


def update_flight_Negative_id_test(FlightDoesNotExistException):
    airline = AirlineCompany(name= 'el al', country_id= 6, user_id= 6)
    flight1 = Flights(id= 11, airline_company_id= 6, origin_country_id= 5, destination_country_id= 5,
               departure_time= 7, landing_time= 3, remaining_tickets= 9)
    FlightDoesNotExistException.add_airline(airline)
    FlightDoesNotExistException.add_flight(flight1)
    flight = Flights(id= -11, airline_company_id= 6, origin_country_id= 5, destination_country_id= 5,
              departure_time=7, landing_time= 3, remaining_tickets= 9)
    with pytest.raises(NegativeDataError):
        FlightDoesNotExistException.update_flight(flight)
        FlightDoesNotExistException.update_flight(flight)
