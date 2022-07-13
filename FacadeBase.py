from abc import ABC, abstractmethod
from Country import Country
from AirlineCompany import AirlineCompany
import params
from Exceptions import UnknownError, PasswordTooShortException, UserAlreadyExistException
from Flights import Flights
from MyLogger import Logger
from User import User


class FacadeBase(ABC):

    @abstractmethod
    def __init__(self, repo, config):
        self.logger = Logger.get_instance()
        self.repo = repo
        self.config = config

    def get_all_flights(self):
        return self.repo.get_all(Flights)

    def get_flight_by_id(self, id):
        return self.repo.get_by_id(Flights, id)

    def get_flights_by_parameters(self, origin_country_id, destination_country_id, date):
        return self.repo.get_by_condition(Flights,
                                          lambda query: query.filter
                                          (Flights.origin_country_id == origin_country_id and
                                           Flights.destination_country_id == destination_country_id and
                                           Flights.departure_time == date))

    def get_all_airlines(self):
        return self.repo.get_all(AirlineCompany)

    def get_airline_by_id(self, id):
        return self.repo.get_by_id(AirlineCompany, id)

    def add_airline(self, airline):
        self.repo.add(airline)

    def get_all_countries(self):
        return self.repo.get_all(Country)

    def get_country_by_id(self, id):
        return self.repo.get_by_id(Country, id)

    def add_user(self, user):
        my_user = self.repo.get_by_column_value(User, User.user_name, user.user_name)
        if my_user:
            self.logger.error(f'User {user.user_name} already exist')
            raise UserAlreadyExistException(user.user_name)
        elif len(user.password) <= params.len1:
            self.logger.error(f'user password must be longer that 4 char')
            raise PasswordTooShortException()
        try:
            self.repo.add(user)
            self.logger.logger.info(f'adding user {user.user_name} successes')
            return user
        except:
            self.logger.logger.error(f'adding user {user.user_name} to the db failed')
            print('failed to add customer')
            raise UnknownError
