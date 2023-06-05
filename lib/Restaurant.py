class Restaurant:
    
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def name(self):
        return self.name
    
    def average_star_rating(self):
        for i in range(len(self.reviews)):
            if i == 0:
                return 0
            else:
                for review in self.reviews:
                   return sum(review.rating)/ len(self.reviews)