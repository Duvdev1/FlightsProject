from AirlineCompany import AirlineCompany
from Country import Country
from db_config import Base, create_all_entities
from sqlalchemy import MetaData, BigInteger, Column, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship, backref

# from db2_config import Base1, create_all_entities

meta = MetaData()


class Flights(Base):
    __tablename__ = 'flights'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    airline_company_id = Column(BigInteger, ForeignKey(AirlineCompany.id), nullable=False)
    origin_country_id = Column(BigInteger, ForeignKey(Country.id), nullable=False)
    destination_country_id = Column(BigInteger, ForeignKey(Country.id), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    landing_time = Column(DateTime, nullable=False)
    remaining_tickets = Column(Integer, nullable=False)

    company = relationship("AirlineCompany", backref=backref("flights", uselist=True))
    origin_country = relationship("Country", foreign_keys=[origin_country_id], uselist=True)
    destination_country = relationship("Country", foreign_keys=[destination_country_id], uselist=True)

    def __repr__(self):
        return f'Flight: (id={self.id}, airline_company_id={self.airline_company_id},' \
               f' origin_country_id={self.origin_country_id}, ' \
               f'destination_country_id={self.destination_country_id}, departure_time={self.departure_time}, ' \
               f'landing_time={self.landing_time},' \
               f' remaining_tickets={self.remaining_tickets})'

    def __str__(self):
        return f'Flight: [id={self.id}, airline_company_id={self.airline_company_id},' \
               f' origin_country_id={self.origin_country_id}, ' \
               f'destination_country_id={self.destination_country_id}, departure_time={self.departure_time}, ' \
               f'landing_time={self.landing_time},' \
               f' remaining_tickets={self.remaining_tickets}]'


create_all_entities()
