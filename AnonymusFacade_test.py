import imp
import pytest
from Customer import Customer
from FacadeBase import FacadeBase
from User import User
from AdministratorFacade import AdministratorFacade
from AirlineCompanyFacade import AirlineCompanyFacade
from AnonymousFacade import AnonymousFacade
from CustomerFacade import CustomerFacade
from DbRepo import DbRepo
from Exceptions import PasswordTooShortException, UserAlreadyExistException
from db2_config import local_session2
from db2_config import config

repo = DbRepo(local_session2)

@pytest.fixture(scope='session')
def anonymous_facade_object():
    anonymous_facade = AnonymousFacade(DbRepo, config)
    return anonymous_facade.login('roy','Aa123456!')


@pytest.fixture(scope='function', autouse=True)
def reset_db(anonymous_facade_object):
    repo.reset_test_db()


def login_success_test(anonymous_facade_object):
    user = User(user_name= 'roy', password= 6555, email= 'duv', user_role= 6)
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 1)
    user_name1 = 'roy'
    password = 6555
    anonymous_facade_object.add_customer(user, customer)
    assert anonymous_facade_object.login(user_name1, password) == True


def login_user_DoesNotExist_test(anonymous_facade_object):
    user_name1 = 'roy'
    password = 65554
    assert anonymous_facade_object.login(user_name1, password) == False


def login_wrong_password_test(anonymous_facade_object):
    user = User(user_name= 'roy', password= 6555, email= 'duv', user_role= 6)
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 1)
    anonymous_facade_object.add_customer(user, customer)
    password = 65224
    user_name = 'roy'
    assert anonymous_facade_object.login(user_name, password) == False


def add_user_success_test(anonymous_facade_object):
    user = User(user_name= 'roy', password= 6555, email= 'duv', user_role= 6)
    customer = Customer (first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 1)
    anonymous_facade_object.add_customer(user, customer)
    my_user = repo.get_by_id(User, user.id)
    assert user in my_user == True


def add_user_passwordTooShort_test(anonymous_facade_object):
    user = User(user_name= 'roy', password= 6, email= 'duv', user_role= 6)
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 1)
    with pytest.raises(PasswordTooShortException):
        anonymous_facade_object.add_customer(user, customer)
        anonymous_facade_object.add_customer(user, customer)


def add_user_AlreadyExist_test(anonymous_facade_object):
    user = User (user_name= 'roy', password= 6, email= 'duv', user_role= 6)
    customer = Customer(first_name= 'roy1', last_name= 'duvdev1', address= 'tel avivs', phone_no= 2354,
                credit_card_no= 1521, user_id= 1)
    with pytest.raises(UserAlreadyExistException):
        anonymous_facade_object.add_customer(user, customer)
        anonymous_facade_object.add_customer(user, customer)
