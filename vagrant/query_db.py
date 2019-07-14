from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
list = session.query(Restaurant).all()
for r in list:
    print r.id, r.name
# veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
# for v in veggieBurgers:
#     print "id: ",v.id
#     print v.restaurant.name
#     print v.price
#     if v.id == 9:
#         v.price = "$2.99"
#         session.add(v)
#         session.commit()
#
# veggies = session.query(MenuItem).filter_by(name = 'Veggie Burger')
# for v in veggies:
#     if v.id == 9:
#         print v.price
