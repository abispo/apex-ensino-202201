
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Profile(Base):

    __tablename__ = 'tb_profiles'

    id = Column(Integer, ForeignKey('tb_users.id'), primary_key=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)

    user = relationship("User", uselist=False, back_populates="profile")
