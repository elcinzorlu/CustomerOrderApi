from sqlalchemy import Column, Integer, String, Float
from . import Base
from sqlalchemy_serializer import SerializerMixin


class CustomerOrder(Base, SerializerMixin):
    __tablename__ = "customer_order"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    barcode = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)
    explanation = Column(String, nullable=False)

    def __init__(self, name, address, barcode, price, amount, explanation):
        self.name = name
        self.address = address
        self.barcode = barcode
        self.price = price
        self.amount = amount
        self.explanation = explanation
