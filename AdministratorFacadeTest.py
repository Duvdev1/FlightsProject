import py
import pytest
from Administrator import Administrator
from AdministratorFacade import AdministratorFacade
from AirlineCompany import AirlineCompany
from AirlineCompanyFacade import AirlineCompanyFacade
from AnonymousFacade import AnonymousFacade
from Customer import Customer
from CustomerFacade import CustomerFacade
from DbRepo import DbRepo
from Exceptions import NegativeDataError, AirlineAlreadyExist, CustomerAlreadyExist, \
    AdministratorAlreadyExist, AirlineDoesNotExist, CustomerDoesNotExist, \
    AdministratorDoesNotExist, PasswordTooShortException, UserAlreadyExistException
from FacadeBase import FacadeBase
from User import User
from db2_config import local_session2
from db_config import local_session
from db_config import config


repo = DbRepo(local_session)

@pytest.fixture(scope='session')
def administrator_facade_object():
    anonymous_facade = AnonymousFacade(DbRepo, config)
    return anonymous_facade.login('roy','Aa123456!')


@pytest.fixture(scope='function',autouse=True)
def reset_db(customer_facade_object):
    customer_facade_object.repo.reset_test_db()
    return

def get_all_customers(administrator_facade_object):
    assert administrator_facade_object.get_all_customers() == repo.get_all(Customer)

def add_airline_success_test(administrator_facade_object):
    user = User(user_name= 'roy', password= 655, email= 'duv', user_role= 6)
    airline = AirlineCompany(name= 'el al', country_id= 6, user_id= 6)
    administrator_facade_object.add_customer(user)
    administrator_facade_object.add_airline(airline)
    check_user = repo.get_by_id(User, 6)
    check_airline = repo.get_by_id(AirlineCompany, 5)
    assert check_airline == airline
    assert check_user == user

def add_airline_failed_test(administrator_facade_object):
    with pytest.raises('InvalidInput'):
        airline = AirlineCompany(name='el al', country_id=6, user_id=6)
        user = ""
        administrator_facade_object.add_customer(user)
        administrator_facade_object.add_airline(airline)
    with pytest.raises('InvalidInput'):
        airline = ""
        user = User(user_name= 'roy', password= 655, email= 'duv', user_role= 6)
        administrator_facade_object.add_customer(user)
        administrator_facade_object.add_airline(airline)
    with pytest.raises(UserAlreadyExistException):
        user = User(user_name= 'roy', password= 655, email= 'duv', user_role= 6)
        airline = AirlineCompany(name= 'el al', country_id= 6, user_id= 6)
        administrator_facade_object.add_customer(user)
        administrator_facade_object.add_airline(airline)
    with pytest.raises(AirlineAlreadyExist):
        user = User(user_name= 'roy', password= 655, email= 'duv', user_role= 6)
        airline = AirlineCompany(name= 'el al', country_id= 6, user_id= 6)
        administrator_facade_object.add_customer(user)
        administrator_facade_object.add_airline(airline)

def add_customer_success_test(administrator_facade_object):
    user = User(user_name= 'roy', password= 655, email= 'duv', user_role= 6)
    customer = Customer(first_name= 'roy',last_name= 'duvdev', address= 'tel aviv', phone_no= 265,
                     credit_card_no= 646, user_id= 7)
    administrator_facade_object.add_customer(customer, user)
    check_customers = repo.get_by_id(Customer, user.id)
    check_user = repo.get_by_id(User, user)
    assert check_customers == customer
    assert check_user == user

def add_customer_failed_test(administrator_facade_object):
    with pytest.raises('InvalidInput'):
        user = User(user_name= 'roy', password= 655, email= 'duv', user_role= 6)
        customer = ""
        administrator_facade_object.add_customer(user, customer)
    with pytest.raises('InvalidInput'):
        user = ""
        customer = Customer(first_name= 'roy',last_name= 'duvdev', address= 'tel aviv', phone_no= 265,
                     credit_card_no= 646, user_id= 7)
        administrator_facade_object.add_customer(user, customer)
    with pytest.raises(PasswordTooShortException):
        user = User(user_name= 'roy', password= 0, email= 'duv', user_role= 6)
        customer = Customer(first_name= 'roy',last_name= 'duvdev', address= 'tel aviv', phone_no= 265,
                     credit_card_no= 646, user_id= 7)
        administrator_facade_object.add_customer(user, customer)
    with pytest.raises(UserAlreadyExistException):
        user = User(user_name= 'roy', password= 0, email= 'duv', user_role= 6)
        customer = Customer(first_name= 'roy',last_name= 'duvdev', address= 'tel aviv', phone_no= 265,
                     credit_card_no= 646, user_id= 7)
        administrator_facade_object.add_user(user)
        administrator_facade_object.add_customer(user, customer)

def add_administrator_success_test(administrator_facade_object):
    admin = Administrator(first_name= 'roy', last_name= 'duv', user_id= 6)
    administrator_facade_object.add_administrator(admin)
    check_admin = repo.get_by_id(admin, user.id)
    check_user = repo.get_by_id(User, user)
    assert check_admin == admin
    assert check_user == user

def add_administrator_failed_test(administrator_facade_object):
    with pytest.raises('InvalidInput'):
        admin = Administrator(first_name= 'roy', last_name= 'duv', user_id= 6)
        administrator_facade_object.add_administrator(admin)
    with pytest.raises('InvalidInput'):
        admin = Administrator(first_name= 'roy', last_name= 'duv', user_id= 6)
        administrator_facade_object.add_administrator(admin)
    with pytest.raises(AdministratorAlreadyExist):
        admin = Administrator(first_name= 'roy', last_name= 'duv', user_id= 6)
        administrator_facade_object.add_administrator(admin)
    with pytest.raises(NegativeDataError):
        admin = Administrator(first_name= 'roy', last_name= 'duv', user_id= -6)
        administrator_facade_object.add_administrator(admin)

def remove_airlineCompany_success_test(administrator_facade_object):
    airline = {'name': 'el al', 'country_id': 6, 'user_id': 6}
    user = {'user_name': 'roy', 'password': 655, 'email': 'duv', 'user_role': 6}
    administrator_facade_object.add_customer(user)
    administrator_facade_object.add_airline(airline)
    administrator_facade_object.remove_airline(airline)
    check_airline = repo.get_by_id(AirlineCompany, airline.id)
    assert check_airline == None

def remove_airlineCompany_failed_test(administrator_facade_object):
    with pytest.raises('InvalidInput'):
        administrator_facade_object.remove_airline('a')
    with pytest.raises(AirlineDoesNotExist):
        administrator_facade_object.remove_airline(55)

def remove_customer_success_test(administrator_facade_object):
    customer = Customer(first_name= 'roy',address= 'tel aviv', phone_no= 265, credit_card_no= 646)
    administrator_facade_object.remove_customer(customer)
    check_customers = repo.get_by_id(Customer, customer.id)
    assert check_customers == None

def remove_customer_failed_test(administrator_facade_object):
     with pytest.raises('InvalidInput'):
        administrator_facade_object.remove_customer('a')
     with pytest.raises(CustomerDoesNotExist):
        administrator_facade_object.remove_customer(7)

def remove_administrator_success_test(administrator_facade_object):
    user = User(user_name= 'roy',password= 655,email= 'duv',user_role= 6)
    admin = Administrator(first_name= 'roy', last_name= 'duv', user_id= 6)
    administrator_facade_object.add_customer(user)
    administrator_facade_object.add_administrator(admin)
    administrator_facade_object.remove_administrator(admin)
    checck_admin = repo.get_by_id(Administrator, admin.id)
    assert admin == checck_admin


def remove_administrator_failed_test(administrator_facade_object):
    with pytest.raises(AdministratorDoesNotExist):
        admin =Administrator(first_name= 'roy', last_name= 'duv', user_id= 6)
        administrator_facade_object.remove_administrator(admin)
        administrator_facade_object.remove_administrator(admin)
    with pytest.raises(NegativeDataError):
        admin = Administrator(first_name= 'roy', last_name= 'duv', user_id= -6)
        administrator_facade_object.remove_administrator(admin)
        administrator_facade_object.remove_administrator(admin)
