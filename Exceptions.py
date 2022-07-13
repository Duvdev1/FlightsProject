class UserAlreadyExistException(Exception):
    def __init__(self, problemtic_user_name, message="user already exist"):
        self.message = message
        self.problemtic_user_name = problemtic_user_name
        super().__init__(self.message)

    def __str__(self):
        return f'UserAlreadyExistException: {self.problemtic_user_name} {self.message}'


class PasswordTooShortException(Exception):
    def __init__(self, message='password is too short, password must be 4 digits/characters minimum'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'PasswordTooShortException: {self.message}'


class NoMoreTicketsForFlightsException(Exception):
    def __init__(self, flight_id, message="no more tickets for this flight"):
        self.flight_id = flight_id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'NoMoreTicketsForFlightsException: {self.flight_id} {self.message}'


class FlightDoesNotExistException(Exception):
    def __init__(self, ticket_id, message='this flight does not exist'):
        self.ticket_id = ticket_id
        self.message = message
        super().__init__(self.message)


class FlightIdAlreadyNotExistException(Exception):
    def __init__(self, ticket_id, message='this flight already exist'):
        self.ticket_id = ticket_id
        self.message = message
        super().__init__(self.message)


class TicketNotFoundException(Exception):
    def __init__(self, ticket_id, message='this ticket does not exist'):
        self.ticket_id = ticket_id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'TicketNotFoundException: {self.ticket_id} {self.message}'


class AirlineAlreadyExist(Exception):
    def __init__(self, problemtic_Airline_id, message="airline already exist"):
        self.message = message
        self.problemtic_user_name = problemtic_Airline_id
        super().__init__(self.message)


class AirlineDoesNotExist(Exception):
    def __init__(self, problemtic_Airline_id, message="airline does not exist"):
        self.message = message
        self.problemtic_user_name = problemtic_Airline_id
        super().__init__(self.message)


class CustomerAlreadyExist(Exception):
    def __init__(self, problematic_customer_id, message="Customer already exist"):
        self.message = message
        self.problematic_customer_id = problematic_customer_id
        super().__init__(self.message)


class AdministratorAlreadyExist(Exception):
    def __init__(self, problematic_admin_id, message="Admin already exist"):
        self.message = message
        self.problematic_admin_id = problematic_admin_id
        super().__init__(self.message)


class AdministratorDoesNotExist(Exception):
    def __init__(self, problematic_admin_id, message="Admin does not exist"):
        self.message = message
        self.problematic_admin_id = problematic_admin_id
        super().__init__(self.message)


class TicketDoesNotExist(Exception):
    def __init__(self, problematic_ticket_id, message="Ticket does not exist"):
        self.message = message
        self.problematic_ticket_id = problematic_ticket_id
        super().__init__(self.message)


class UnknownError(Exception):
    def __init__(self, message="airline does not exist"):
        self.message = message
        super().__init__(self.message)


class CustomerDoesNotExist(Exception):
    def __init__(self, customer_id, message="customer id does not exist"):
        self.message = message
        self.customer_id = customer_id
        super().__init__(self.message)


class NegativeDataError(Exception):
    def __init__(self, message="negative data is invalid"):
        self.message = message
        super().__init__(self.message)


class UserRoleTableError(Exception):
    def __init__(self, msg="Cannot have more than 3 roles in the user_roles table."):
        self.msg = msg
        super().__init__(self.msg)


class CountryAlreadyExist(Exception):
    def __init__(self, problematic_country_name, message="Country already exist"):
        self.message = message
        self.problematic_country_name = problematic_country_name
        super().__init__(self.message)
