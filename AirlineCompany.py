from Country import Country
from User import User
from db_config import Base, create_all_entities
from sqlalchemy import MetaData, String, Column, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

from db2_config import Base1, create_all_entities

meta = MetaData()


class AirlineCompany(Base):
    __tablename__ = 'airline_companies'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    country_id = Column(BigInteger, ForeignKey(Country.id), nullable=False)
    user_id = Column(BigInteger, ForeignKey(User.id), nullable=False, unique=True)

    country = relationship("Country", backref=backref("AirlineCompany", uselist=True))
    user = relationship("User", backref=backref("AirlineCompany", uselist=True))

    def __repr__(self):
        return f'AirlineCompany: (id={self.id}, name={self.name}, country_id={self.country_id}, ' \
               f'user_id={self.user_id})'

    def __str__(self):
        return f'AirlineCompany: [id={self.id}, name={self.name}, country_id={self.country_id}, ' \
               f'user_id={self.user_id}]'


create_all_entities()
