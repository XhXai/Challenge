from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///review.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return session.query(cls).all()

# Create the database tables
Base.metadata.create_all(engine)
