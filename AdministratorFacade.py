import params
from Administrator import Administrator
from AirlineCompany import AirlineCompany
from Customer import Customer
from Exceptions import CustomerDoesNotExist, UnknownError, AirlineAlreadyExist, \
    CustomerAlreadyExist, \
    NegativeDataError, AdministratorAlreadyExist, AirlineDoesNotExist, AdministratorDoesNotExist, CountryAlreadyExist
from FacadeBase import FacadeBase
from Country import Country


class AdministratorFacade(FacadeBase):
    def __init__(self, login_token, repo, config):
        super().__init__(repo, config)
        self._login_token = login_token

    def get_all_customers(self):
        self.logger.logger.info(f'AdministratorFacade: getting all customers')
        if self._login_token.role == 'Administrator':
            customers = self.repo.get_all(Customer)
            if customers is None:
                print('there are no customers')
                self.logger.logger.error(f'AdministratorFacade: there are no customers exist')
                raise CustomerDoesNotExist
            else:
                try:
                    return self.repo.get_all(Customer)
                except:
                    self.logger.logger.error(f'AdministratorFacade: could not get customers')
                    print("An unexpected Error occurred")
                    raise UnknownError

    def add_airline(self, airline):
        self.logger.logger.info(f'AdministratorFacade: adding airline by id {airline.id}')
        if self._login_token.role != 'Administrator':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_airline = self.repo.get_by_id(AirlineCompany, airline.id)
        if my_airline is None:
            try:
                self.repo.add(airline)
                self.logger.logger.info(f'AdministratorFacade: airline add successfully')
            except:
                self.logger.logger.error(f'AdministratorFacade: Failed to add airline')
                print("An Error occurred")
                raise UnknownError
        else:
            self.logger.logger.error(f'AdministratorFacade: airline id {AirlineCompany.id} already exist')
            raise AirlineAlreadyExist

    def add_customer(self, customer):
        self.logger.logger.info(f'AdministratorFacade: adding customer by id {customer.id}')
        if self._login_token.role != 'Administrator':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_customer = self.repo.get_by_id(Customer, Customer.id)
        if my_customer is None:
            try:
                self.repo.add(customer)
                self.logger.logger.info(f'AdministratorFacade: customer add successfully')
            except:
                print("An Error occurred")
                raise UnknownError
        else:
            print('customer already exist')
            self.logger.logger.error(f'AdministratorFacade: customer {Customer.id} already exist')
            raise CustomerAlreadyExist

    def add_administrator(self, administrator):
        self.logger.logger.info(f'AdministratorFacade: adding administrator by id {administrator.id}')
        if self._login_token.role != 'Administrator':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        try:
            self.repo.add(administrator)
            self.logger.logger.info(f'AdministratorFacade: admin {administrator.id} add successfully')
        except:
            print("An Error occurred, admin id already exist")
            #  self.MyLogger.print_error_log(f'AdministratorFacade: admin id {Administrator.id} already exist')
            raise AdministratorAlreadyExist

    def remove_airline(self, airline):
        self.logger.logger.info(f'AdministratorFacade: removing airline by id {airline.id}')
        if self._login_token.role != 'Administrator':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_airline = self.repo.get_by_id(AirlineCompany, airline.id)
        if my_airline is None:
            print('airline does not exist')
            self.logger.logger.error(f'AdministratorFacade: airline {airline.id} does not exist')
            raise AirlineDoesNotExist
        elif my_airline:
            try:
                self.repo.delete_by_id(AirlineCompany, AirlineCompany.id, airline.id)
                self.logger.logger.info(f'AdministratorFacade: airline deleted successfully')
            except:
                print("An unexpected Error occurred")
                self.logger.logger.error(f'something went wrong')
                raise UnknownError
        my_airline = self.repo.get_by_id(AirlineCompany, airline.id)
        self.logger.logger.info(f'AirlineCompanyFacade: checking for airline removal by id {airline.id}')
        if my_airline is None:
            print('airline removed successfully')
            self.logger.logger.info(f'AirlineCompanyFacade: airline removed')

    def remove_customer(self, customer):
        self.logger.logger.info(f'AdministratorFacade: removing customer by id {customer.id}')
        if self._login_token.role != 'Administrator':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_customer = self.repo.get_by_id(Customer, customer.id)
        if my_customer is None:
            print('customer does not exist')
            self.logger.logger.error(f'customer {customer.id} does not exist')
            raise CustomerDoesNotExist
        elif my_customer:
            try:
                self.repo.delete_by_id(Customer, Customer.id, customer.id)
                self.logger.logger.info(f'AdministratorFacade: customer {Customer.id} deleted successfully')
            except:
                self.logger.logger.error(f'AdministratorFacade: could not remove customer')
                print("An unexpected Error occurred")
                raise UnknownError
        my_customer = self.repo.get_by_id(Customer, customer.id)
        if my_customer is None:
            print('customer deleted successfully')
            self.logger.logger.info(f'AdministratorFacade: customer id {customer.id} deleted successfully')

    def remove_administrator(self, administrator):
        self.logger.logger.info(f'AdministratorFacade: removing administrator by id {administrator.id}')
        if self._login_token.role != 'Administrator':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_administrator = self.repo.get_by_id(Administrator, Administrator.id)
        if my_administrator < 0:
            print('admin id cannot be negative')
            self.logger.logger.error(f'AdministratorFacade: admin id cannot be negative')
            raise NegativeDataError
        elif my_administrator is None:
            print('admin id does not exist')
            self.logger.logger.error(f'AdministratorFacade: admin id {administrator.id} does not exist')
            raise AdministratorDoesNotExist
        elif my_administrator:
            try:
                self.repo.delete_by_id(Administrator, Administrator.id, administrator.id)
                self.logger.logger.info(
                    f'AdministratorFacade: administrator {Administrator.id} removed successfully')
            except:
                print("An unexpected Error occurred")
                self.logger.logger.error(f'AdministratorFacade: an error occurred')
                raise UnknownError
        my_administrator = self.repo.get_by_id(Administrator, Administrator.id)
        if my_administrator is None:
            print('admin removed successfully')
            self.logger.logger.info(f'AdministratorFacade: admin id {administrator.id} removed successfully')

    def add_country(self, name):
        self.logger.logger.info(f'AdministratorFacade: adding country by name {name}')
        if self._login_token.role != 'Administrator':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_country = self.repo.get_name(Country, Country.name, name)
        print(my_country)
        self.repo.add_co(Country, name)
        if not my_country:
            try:
                self.repo.add_co(Country, name)
                self.repo.add(name)
                self.logger.logger.info(f'AdministratorFacade: country add successfully')
            except:
                self.logger.logger.error(f'AdministratorFacade: Failed to add country')
                print("An Error occurred")
                raise UnknownError
        else:
            self.logger.logger.error(f'AdministratorFacade: airline id {AirlineCompany.id} already exist')
            return "a"
