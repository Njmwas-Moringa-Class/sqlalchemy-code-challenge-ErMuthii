from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete existing data
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()


    print('Seeding database 🌱🌱🌱')

# Create some restaurants
restaurant1 = Restaurant(name="Restaurant A", price=3)
restaurant2 = Restaurant(name="Restaurant B", price=2)
restaurant3 = Restaurant(name="Restaurant C", price=4)

# Add the restaurants to the session
session.add_all([restaurant1, restaurant2, restaurant3])
session.commit()

# Create some customers
customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Smith")
customer3 = Customer(first_name="Alice", last_name="Johnson")

# Add the customers to the session
session.add_all([customer1, customer2, customer3])
session.commit()

# Create some reviews
review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=4)
review2 = Review(restaurant=restaurant2, customer=customer2, star_rating=5)
review3 = Review(restaurant=restaurant3, customer=customer3, star_rating=3)

# Add the reviews to the session
session.add_all([review1, review2, review3])
session.commit()

# Close the session
session.close()
