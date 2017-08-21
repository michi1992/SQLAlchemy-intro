import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = create_engine()

class Restaurant(Base):
    # __tablename is a special variable that will be used to create a table
    __tablename__ = 'restaurant'

    # map python objects to columns in our database
    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    # This is how you create relationships in SQLAlchemy:
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


#################### insert at the end of the file ############################
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)