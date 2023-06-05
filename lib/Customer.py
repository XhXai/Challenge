class Customer:

    customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.customers.append(self)
        self.reviews = []


    def given_name(self):
        return self.first_name
    
    def family_name(self):
        return self.last_name
    
    def full_name(self):
        return self.first_name + '' + self.last_name
    
    @classmethod
    def all(cls):
        return cls.customers
    
    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
            else:
                return None
            
    @classmethod
    def find_all_by_given_name(cls, name):
        found_name = []
        for customer in cls.customers:
            if customer.given_name() == name:
                found_name.append(customer)
        
        return found_name
            
    def __str__(self):
        return f"Customer Name: - {self.full_name}"
     
a = Customer('Ronny', 'Luvega')







