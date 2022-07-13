from Customer import Customer
from Flights import Flights
from db_config import Base, create_all_entities
from sqlalchemy import MetaData, Column, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

# from db2_config import Base1, create_all_entities

meta = MetaData()


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    flight_id = Column(BigInteger, ForeignKey(Flights.id), nullable=False)
    customer_id = Column(BigInteger, ForeignKey(Customer.id), nullable=False)

    flight = relationship("Flights", backref=backref("Ticket", uselist=True))
    customer = relationship("Customer", backref=backref("Ticket", uselist=True))

    def __repr__(self):
        return f'Ticket: (id={self.id}, flight_id={self.flight_id},' \
               f' customer_id={self.customer_id})'

    def __str__(self):
        return f'Ticket: [id={self.id}, flight_id={self.flight_id},' \
               f' customer_id={self.customer_id}]'


create_all_entities()
