from AirlineCompany import AirlineCompany
from Exceptions import FlightDoesNotExistException, AirlineDoesNotExist, \
    UnknownError, AirlineAlreadyExist, NegativeDataError
from FacadeBase import FacadeBase
from Flights import Flights


class AirlineCompanyFacade(FacadeBase):
    def __init__(self, login_token, repo, config):
        super().__init__(repo, config)
        self._login_token = login_token

    def add_flight(self, flight):
        self.logger.logger.info(f'AirlineCompanyFacade: adding {flight}')
        if self._login_token.role != 'AirlineCompany':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_flight = self.repo.get_by_column_value(Flights, Flights.id, flight.id)
        if my_flight:
            self.logger.logger.error(f'AirlineCompanyFacade: {flight.id} already exist')
            raise AirlineAlreadyExist(flight.id)
        try:
            self.repo.add(flight)
            self.logger.logger.info(f'AirlineCompanyFacade: adding flight {flight.id} successes')
        except:
            self.logger.logger.error(f'AirlineCompanyFacade: adding flight {flight.id} to the db failed')
            raise UnknownError

    def remove_flight(self, flight):
        self.logger.logger.info(f'AirlineCompanyFacade: removing flight by id {flight.id}')
        if self._login_token.role != 'AirlineCompany':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_flight = self.repo.get_by_id(Flights, flight.id)
        if my_flight is None:
            print('airline does not exist')
            self.logger.logger.error(f'AirlineCompanyFacade: flight {flight.id} does not exist')
            raise FlightDoesNotExistException
        elif my_flight:
            try:
                self.repo.delete_by_id(Flights, Flights.id, flight.id)
                self.logger.logger.info(f'AirlineCompanyFacade: flight deleted successfully')
            except:
                print("An unexpected Error occurred")
                self.logger.logger.error(f'AirlineCompanyFacade: something went wrong')
                raise UnknownError
        my_flight = self.repo.get_by_id(AirlineCompany, flight.id)
        self.logger.logger.info(f'AirlineCompanyFacade: checking for flight removal by id {flight.id}')
        if my_flight is None:
            print('airline removed successfully')
            self.logger.logger.info(f'AirlineCompanyFacade: flight removed')

    def get_flights_by_airline(self, airline):
        self.logger.logger.info(f'AirlineCompanyFacade: getting flight by id {airline.id}')
        if self._login_token.role != 'AirlineCompany':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_airline = self.repo.get_by_id(AirlineCompany, airline.id)
        if my_airline:
            try:
                return self.repo.get_by_column_value(Flights, Flights.airline_company_id, airline.id)
            except:
                self.logger.logger.error(f'airline {airline} does not exist')
                print("airline does not exist")
                raise AirlineDoesNotExist

    def update_airline(self, airline):
        self.logger.logger.info(f'AirlineCompanyFacade: updating airline {airline.id}')
        self.logger.logger.info(f'AirlineCompanyFacade: getting airline by id {airline.id}')
        if self._login_token.role != 'AirlineCompany':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_old_airline_id = self.repo.get_by_id(AirlineCompany, airline.id)
        my_airline_id = self.repo.get_by_id(AirlineCompany, airline.id)
        if my_airline_id:
            try:
                self.repo.update_by_id(AirlineCompany, airline)
            except:
                if my_airline_id is None:
                    print("airline does not exist")
                    raise AirlineDoesNotExist
                elif my_old_airline_id == my_airline_id:
                    self.logger.logger.error(f'AirlineCompanyFacade: could not update airline')
                else:
                    print("An exception occurred when we try update customer")
                    raise UnknownError

    def update_flight(self, flights):
        self.logger.logger.info(f'AirlineCompanyFacade: updating flight')
        if self._login_token.role != 'AirlineCompany':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_flight = self.repo.get_by_id(Flights, Flights.id)
        my_old_flight_id = self.repo.get_by_id(Flights, Flights.id)
        if my_flight:
            try:
                self.repo.update_by_id(Flights, flights)
                self.logger.logger.info(f'AirlineCompanyFacade: updating flight by id')
            except:
                if my_flight is None:
                    print('flight does not exist')
                    raise FlightDoesNotExistException
                elif my_flight.id == my_old_flight_id.id:
                    self.logger.logger.error(f'AirlineCompanyFacade: could not update flight')
                else:
                    print("An exception occurred when we try update customer")
                    raise UnknownError
