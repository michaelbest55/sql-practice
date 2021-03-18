from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Profile(Base):
    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, nullable=True)
    company = Column(String, nullable=True)
    ssn = Column(String, nullable=True)
    residence = Column(String, nullable=True)
    blood_group = Column(String, nullable=True)
    website = Column(String, nullable=True)
    username = Column(String, nullable=True)
    name = Column(String, nullable=True)
    sex = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, nullable=True)
    birthdate = Column(String, nullable=True)
