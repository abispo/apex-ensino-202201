from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base
from models.order import orders_products


class Product(Base):

    __tablename__ = 'tb_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)

    orders = relationship("Order", secondary=orders_products, back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name})>"