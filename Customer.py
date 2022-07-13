from User import User
from db_config import Base, create_all_entities
from sqlalchemy import MetaData, String, Column, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

# from db2_config import Base1, create_all_entities

meta = MetaData()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    phone_no = Column(String, nullable=False, unique=True)
    credit_card_no = Column(String, nullable=False, unique=True)
    user_id = Column(BigInteger, ForeignKey(User.id), nullable=False, unique=True)

    user = relationship("User", backref=backref("Customer", uselist=True))

    def __repr__(self):
        return f'Customer: (id={self.id}, first_name={self.first_name}, last_name={self.last_name}, ' \
               f'address={self.address}, phone_no={self.phone_no}, credit_card_no={self.credit_card_no},' \
               f' user_id={self.user_id})'

    def __str__(self):
        return f'Customer: [id={self.id}, first_name={self.first_name}, last_name={self.last_name}, ' \
               f'address={self.address}, phone_no={self.phone_no}, credit_card_no={self.credit_card_no},' \
               f' user_id={self.user_id}]'


create_all_entities()
