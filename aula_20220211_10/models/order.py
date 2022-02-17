from sqlalchemy import Column, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship

from database import Base

orders_products = Table('tb_orders_products', Base.metadata,
                        Column('order_id', Integer, ForeignKey('tb_orders.id'), primary_key=True),
                        Column('product_id', Integer, ForeignKey('tb_products.id'), primary_key=True))


class Order(Base):

    __tablename__ = 'tb_orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)

    user = relationship("User", uselist=False, back_populates="orders")
    products = relationship("Product", secondary=orders_products, back_populates="orders")

    def __repr__(self):
        return f"<Order(id={self.id}, timestamp={self.timestamp})>"