from User import User
from db_config import Base, create_all_entities
from sqlalchemy import MetaData, String, Column, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

# from db2_config import Base1, create_all_entities

meta = MetaData()


class Administrator(Base):
    __tablename__ = 'administrators'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_id = Column(BigInteger, ForeignKey(User.id), unique=True, nullable=False)

    user = relationship("User", backref=backref("Administrator", uselist=False))

    def __repr__(self):
        return f'Administrator: (id={self.id}, first_name={self.first_name}, last_name={self.last_name}, ' \
               f'user_id={self.user_id})'

    def __str__(self):
        return f'Administrator: [id={self.id}, first_name={self.first_name}, last_name={self.last_name}, ' \
               f'user_id={self.user_id}]'


create_all_entities()
