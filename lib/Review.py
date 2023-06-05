class Review:
    
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.reviews.append(self)
        

    def Review_rating(self):
        return self.rating
    
    def all(cls):
        return cls.reviews
    
    def __str__(self):
        return f"Review: Customer - {self.customer}, Restaurant - {self.restaurant}, Rating - {self.rating}"
    
t = Review('Ronny', 'Kibanda', 3)
j = Review('Jemo', 'Kempinsky', 5)

print(t)
print(j)









