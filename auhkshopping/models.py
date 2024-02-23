from . import db

class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    description = db.Column(db.String(500), nullable = False)
    image = db.Column(db.String(60), nullable = False, default = 'defaultbrand.jpg')
    product = db.relationship('Product', backref = 'Brand', cascade = "all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}\n"
        str = str.format(self.id, self.name, self .description, self.image)
        return str

orderdetails = db.Table('orderdetails',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable = False),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), nullable = False),
    db.PrimaryKeyConstraint('order_id', 'product_id'))

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, Date:{}, Brand: {}\n"
        str = str.format(self.id, self.name, self .description, self.image, self.price, self.date, self.brand_id)
        return str

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    shippingaddress = db.Column(db.String(128))
    billingaddress = db.Column(db.String(128))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    products = db.relationship("Product", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "Id: {}, Status: {}, Firstname: {}, Lastname: {}, Email: {}, Phone: {}, Shipping Address: {}, Billing Address: {}, Date: {}, Products: {}, Total Cost: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.lastname, self.email, self.shippingaddress, self.billingaddress, self.phone, self.date, self.products, self.totalcost)
        return str