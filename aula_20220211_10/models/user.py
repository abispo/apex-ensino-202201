from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    passwd = Column(String(200), nullable=False)

    profile = relationship("Profile", uselist=False, back_populates="user")
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
