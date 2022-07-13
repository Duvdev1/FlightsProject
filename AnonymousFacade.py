from Exceptions import UserRoleTableError
from FacadeBase import FacadeBase
from LoginToken import LoginToken
from User import User


class AnonymousFacade(FacadeBase):

    def __init__(self, repo, config):
        super().__init__(repo, config)

    def login(self, username1, password1):
        print("start")
        user = self.repo.get_by_condition(User, lambda query: query.filter(User.user_name == username1,
                                                                           User.password == password1).first())

        print("error1")
       # if not user:
        #    self.logger.logger.info(f'Wrong username {username1} '
         #                           f'or password {password1} has been entered to the login function.')

        print("error2")
        print(user.user_role_id)
        print(user)

            #return
        logged_in_user = user
        if logged_in_user.user_role_id == 1:
            print("f")
            token_dic = {'id': logged_in_user.id, 'name': username1, 'role': 'Administrator'}
        elif logged_in_user.user_role_id == 2:
            token_dic = {'id': logged_in_user.id, 'name': username1, 'role': 'Customer'}
        elif logged_in_user.user_role_id == 3:
            token_dic = {'id': logged_in_user.id, 'name': username1, 'role': 'AirlineCompany'}
        else:
            self.logger.logger.info(f'User Roles table contains more than 3 user roles. Please check it ASAP.')
            raise UserRoleTableError
        login_token = LoginToken(token_dic['id'], token_dic['name'],
                                 token_dic['role'])
        self.logger.logger.info(f'{login_token} logged in to the system.')
        print(login_token)
        return login_token

    def add_customer(self, user, customer):
        self.logger.logger.info(f'AnonymousFacade: adding customer: {user}')
        self.add_user(user)
        customer.user_id = user.id
        self.repo.add(customer)

    def add_user(self, user):
        self.repo.add(user)
