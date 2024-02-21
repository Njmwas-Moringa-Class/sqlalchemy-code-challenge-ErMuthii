# import os
# import sys

# sys.path.append(os.getcwd)

# from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer,ForeignKey)
# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()
# engine = create_engine('sqlite:///db/restaurants.db', echo=True)


# class Review(Base):
#     __tablename__ = "reviews"

#     id = Column(Integer, primary_key=True)
#     star_rating = Column(Integer())

#     restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
#     customer_id = Column(Integer(), ForeignKey('customers.id'))

#     restaurant = relationship('Restaurant', backref=backref('reviews'))
#     customer = relationship('Customer', backref=backref('reviews'))

#     def __repr__(self):
#         return f'Review(star rating={self.star_rating},' + \
#                f'Restaurant ID ={self.restaurant_id}.' + \
#                f'Customer ID = {self.customer_id})' 
    
#     def customer(self):
#         return self.customer
    
#     def restaurant(self):
#         return self.restaurant


# class Restaurant(Base):
#     __tablename__ = 'restaurants'

#     id = Column(Integer, primary_key=True)
#     name = Column(String())
#     price = Column(Integer)

#     def __repr__(self):
#         return f'Restaurant: {self.name}'
    
#     def reviews(self):
#         return self.reviews
    
#     def restaurants(self):
#         return[ review.restaurant for review in self.reviews]
    
    

# class Customer(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String())
#     last_name = Column(String())

#     def __repr__(self):
#         return f'Customer: {self.name}'
    
#     def reviews(self):
#         return self.reviews
    
#     def restaurants(self):
#         return [review.restaurants for review in self.reviews]
    
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
    
#     def favorite_restaurant(self):
#         if not self.reviews:
#             return None
#         return max(self.reviews, key=lambda review: review.star_rating).restaurant

#     def add_review(self, restaurant, rating):
#         new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
#         return new_review

#     def delete_reviews(self, restaurant):
#         reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
#         for review in reviews_to_delete:
#             review.customer = None
#             review.restaurant = None
#             review.star_rating = None
#             review.customer_id = None
#             review.restaurant_id = None
    
import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer())

    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', backref='reviews')
    customer = relationship('Customer', backref='reviews')

    def __repr__(self):
        return f'Review(star rating={self.star_rating},' + \
               f'Restaurant ID ={self.restaurant_id}.' + \
               f'Customer ID = {self.customer_id})'
    
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant


    
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
    


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    def __repr__(self):
        return f'Restaurant: {self.name}'

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return [review.customer for review in self.reviews]
    
    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        reviews = []
        for review in self.reviews:
            review_str = f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars."
            reviews.append(review_str)
        return reviews


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'Customer: {self.first_name} {self.last_name}'

    def get_reviews(self):
        return self.reviews

    def get_restaurants(self):
        return [review.restaurant for review in self.reviews]

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def favorite_restaurant(self):
        if not self.reviews:
            return None
        return max(self.reviews, key=lambda review: review.star_rating).restaurant

    def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        return new_review

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            review.customer = None
            review.restaurant = None
            review.star_rating = None
            review.customer_id = None
            review.restaurant_id = None
