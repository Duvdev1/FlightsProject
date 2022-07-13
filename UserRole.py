from db_config import Base, create_all_entities
from sqlalchemy import MetaData, String, Column, BigInteger

# from db2_config import Base1, create_all_entities

meta = MetaData()


class UserRole(Base):
    __tablename__ = 'user_roles'
    id = Column(BigInteger, primary_key=True)
    role_name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'UserRole: (id={self.id}, role_name={self.role_name})'

    def __str__(self):
        return f'UserRole: [id={self.id}, role_name={self.role_name}]'


create_all_entities()
