from Tools.scripts.fixnotice import process
from sqlalchemy import Column, Integer, String, Float, DataTime, ForeignKey
from sqlalchemy.orm import relationship

from backend.database import Base

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True)
    value = Column(Float, nulable=False)
    period = Column(DataTime, nulable=False)

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    start_date = Column (DataTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    price_id = Column(Integer, ForeignKey('prices.id'))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String, nulable=False)
    password = Column(String, nulable=False)
    mail = Column(String, nulable=False)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    basket = relationship("Basket", back_populates="users")

class Basket(Base):
    __tablename__ = "baskets"
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
