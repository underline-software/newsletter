import uuid
from sqlalchemy import Column, UniqueConstraint, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class register(Base):
    __tablename__ = 'register'
    id = Column(String(255), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    __table_args__ = (UniqueConstraint('name', 'email', name='_session_email_unq'),)
