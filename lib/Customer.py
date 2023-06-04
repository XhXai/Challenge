from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'


    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    

    @classmethod
    def all(cls):
        return session.query(cls).all()
    
# Create the database tables
engine = create_engine('sqlite:///customer.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a new customer
customer1 = Customer("George", "Washington")

# Add the customer to the session and commit it to the database
session.add(customer1)
session.commit()

# Retrieve all customers from the database
# all_customers = Customer.all(session)
# for customer in all_customers:
#     print(customer.full_name())

# Update a customer's given name
customer1.given_name = "George"
session.commit()

# Print the updated customer's full name
print(customer1.full_name())





    
    
        
    
        
        