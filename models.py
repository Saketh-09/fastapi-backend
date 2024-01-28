from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Connect(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    last_name = Column(String, unique=True, index=True)
    first_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    comment = Column(String, unique=True, index=True)
