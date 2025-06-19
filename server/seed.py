from app import db, create_app
from models import Customer, Item, Review

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Customer(name="Tal Yuri")
    c2 = Customer(name="Nash Swift")

    i1 = Item(name="Laptop Backpack", price=49.99)
    i2 = Item(name="Insulated Coffee Mug", price=9.99)

    r1 = Review(comment="Great quality", customer=c1, item=i1)
    r2 = Review(comment="Keeps drinks hot", customer=c1, item=i2)
    r3 = Review(comment="Stylish design", customer=c2, item=i1)

    db.session.add_all([c1, c2, i1, i2, r1, r2, r3])
    db.session.commit()
