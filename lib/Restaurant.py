from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String)  # Renamed the column to 'restaurant_name'

    def __init__(self, name):
        self.restaurant_name = name  # Updated the attribute name

    def get_name(self):  # Renamed the method to 'get_name'
        return self.restaurant_name

# Create the database tables
engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a new restaurant
restaurant1 = Restaurant("ABC Restaurant")

# Add the restaurant to the session and commit it to the database
session.add(restaurant1)
session.commit()

# Retrieve the restaurant's name from the database
restaurant_name = restaurant1.get_name()  # Call the method to get the name
print(restaurant_name)

    
        