from UserRole import UserRole
from db_config import Base, create_all_entities
from sqlalchemy import MetaData, String, Column, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

# from db2_config import Base1, create_all_entities

meta = MetaData()


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=False)
    user_role_id = Column(BigInteger, ForeignKey(UserRole.id), nullable=False)

    UserRole = relationship("UserRole", backref=backref("User", uselist=True))

    def __repr__(self):
        return f'User: (id={self.id}, user_name={self.user_name},' \
               f' password={self.password}, ' \
               f'email={self.email}, user_role={self.user_role_id})'

    def __str__(self):
        return f'User: [id={self.id}, user_name={self.user_name},' \
               f' password={self.password}, ' \
               f'email={self.email}, user_role={self.user_role_id}]'


create_all_entities()
