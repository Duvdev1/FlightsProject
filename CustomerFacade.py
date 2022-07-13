from User import User
from Customer import Customer
from Exceptions import TicketNotFoundException, UnknownError, \
    CustomerDoesNotExist, NegativeDataError, FlightDoesNotExistException
from FacadeBase import FacadeBase
from Ticket import Ticket


class CustomerFacade(FacadeBase):

    def __init__(self, login_token, repo, config):
        super().__init__(repo, config)
        self._login_token = login_token

    def update_customer(self, customer):
        self.logger.logger.info(f'CustomerFacade: updating customer {customer}')
        if self._login_token.role != 'Customer':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_customer = self.repo.get_by_id(Customer, customer.id)
        if my_customer:
            try:
                self.repo.update_by_id(User, customer)
            except:
                self.logger.logger.error(f'CustomerFacade: customer could not be updated')
                print("An exception occurred when we try update customer")
                raise UnknownError

    def add_ticket(self, ticket):
        self.logger.logger.info(f'CustomerFacade: adding ticket {ticket}')
        if self._login_token.role != 'Customer':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        if ticket.customer_id < 0:
            self.logger.logger.error(f'CustomerFacade: customer id is negative')
        elif ticket.customer_id != self._login_token.id:
            self.logger.logger.error(f'CustomerFacade: customer id is not yours')
        elif ticket.flight_id < 0:
            self.logger.logger.error(f'CustomerFacade: flight id is negative')
            print("customer does not exist")
        else:
            try:
                self.logger.logger.info(f'CustomerFacade: adding ticket')
                self.repo.add(ticket)
                new_ticket = self.repo.get_by_id(Ticket, Ticket.id)
                if new_ticket:
                    self.logger.logger.info(f'CustomerFacade: ticket add successfully')
                    print('ticket add successfully')
            except:
                self.logger.logger.error(f'CustomerFacade: unexpected error')
                print("An exception occurred when we try add ticket")
                raise UnknownError

    def remove_ticket(self, ticket):
        self.logger.logger.info(f'CustomerFacade: removing ticket {ticket}')
        if self._login_token.role != 'Customer':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_ticket = self.repo.get_by_id(Ticket, ticket.id)
        if my_ticket is None:
            print("ticket does not exist, failed to remove")
            raise TicketNotFoundException
        elif my_ticket.customer_id == self._login_token.id:
            try:
                self.logger.logger.info(f'CustomerFacade: deleting ticket by id {ticket.id}')
                self.repo.delete_by_id(Ticket, Ticket.id, ticket.id)
            except:
                if Ticket.id:
                    self.logger.logger.error(f'CustomerFacade: could not remove ticket')
                    raise UnknownError

    def get_tickets_by_customer(self, customer):
        self.logger.logger.info(f'CustomerFacade: getting tickets by customer id {customer.id}')
        if self._login_token.role != 'Customer':
            self.logger.logger.error(f'The login token is not correct for this function,'
                                     f' the login token is "{self._login_token}"')
            return
        my_customer = self.repo.get_by_id(Customer, customer.id)
        if len(customer.id) < 0:
            self.logger.logger.error(f'CustomerFacade: customer id is negative')
            print("customer id is negative")
            raise NegativeDataError
        elif my_customer.id != customer.id:
            self.logger.logger.error(f'CustomerFacade: get_tickets_by_customer - customer id is not yours')
        elif my_customer is None:
            print('customer does not exist')
            self.logger.logger.error(f'CustomerFacade: customer {customer.id} does not exist')
            raise CustomerDoesNotExist
        else:
            try:
                return self.repo.get_by_column_value(Ticket, Ticket.customer_id, customer.id)
            except:
                self.logger.logger.error(f'something went wrong, unable to get ticket by customer')
                print("could not get ticket, something went wrong")
                raise UnknownError
