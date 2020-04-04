from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)

    habits = relationship("HabitModel", back_populates="user")
