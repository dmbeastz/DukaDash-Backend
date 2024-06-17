from sqlalchemy_serializer import SerializerMixin
from enum import Enum
from sqlalchemy.orm import validates
from datetime import datetime
import re
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class MerchantStatus(Enum):
    OFFLINE = 'Offline'
    ONLINE = 'Online'

class Merchant(db.Model, SerializerMixin):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column('password', db.String(100), nullable=False)  # Use _password to store the hashed password
    image = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(100), default='merchant', nullable=False)
    status = db.Column(db.Enum(MerchantStatus), default=MerchantStatus.ONLINE, nullable=True)
    
    stores = db.relationship('Store', backref='merchant', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        assert re.match(r"[^@]+@[^@]+\.[^@]+", email), "Invalid email format"
        return email

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'image': self.image,
            'role': self.role,
            'status': self.status
        }

    def __repr__(self):
        return f"<User {self.id}, {self.username}, {self.role}, {self.email}>"

class Store(db.Model, SerializerMixin):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    image = db.Column(db.String(100), nullable=True)
    total_revenue = db.Column(db.Integer, nullable=True)
    net_profit = db.Column(db.Integer, nullable=True)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'), nullable=False)
    
    payments = db.relationship('Payment', backref='store', lazy=True)
    requests = db.relationship('Request', backref='store', lazy=True)
    products = db.relationship('Product', backref='store', lazy=True)
    admins = db.relationship('Admin', backref='store', lazy=True)
    clerks = db.relationship('Clerk', backref='store', lazy=True)

class EmployeesStatus(Enum):
    OFFLINE = 'Offline'
    ONLINE = 'Online'
    DEACTIVATED = 'Deactivated'
    ON_LEAVE = 'On_Leave'

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column('password', db.String(100), nullable=False)  # Use _password to store the hashed password
    image = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(100), default='admin', nullable=False)
    status = db.Column(db.Enum(EmployeesStatus), default=EmployeesStatus.ONLINE)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        assert re.match(r"[^@]+@[^@]+\.[^@]+", email), "Invalid email format"
        return email

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'image': self.image,
            'role': self.role,
            'status': self.status
        }

    def __repr__(self):
        return f"<User {self.id}, {self.username}, {self.role}, {self.email}>"

class Clerk(db.Model, SerializerMixin):
    __tablename__ = 'clerks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column('password', db.String(100), nullable=False)  # Use _password to store the hashed password
    image = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(100), default='clerk', nullable=False)
    status = db.Column(db.Enum(EmployeesStatus), default=EmployeesStatus.ONLINE)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        assert re.match(r"[^@]+@[^@]+\.[^@]+", email), "Invalid email format"
        return email

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'image': self.image,
            'role': self.role,
            'status': self.status
        }

    def __repr__(self):
        return f"<User {self.id}, {self.username}, {self.role}, {self.email}>"

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    condition = db.Column(db.String(100), nullable=True)
    stock_quantity = db.Column(db.Integer, nullable=True, default=0)
    spoil_quantity = db.Column(db.Integer, nullable=True, default=0)
    buying_price = db.Column(db.Integer, nullable=True)
    selling_price = db.Column(db.Integer, nullable=True)
    sales = db.Column(db.Integer, nullable=True)
    sales_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': self.price,
            'condition': self.condition,
            'stock_quantity': self.stock_quantity,
            'spoilt_quantity': self.spoil_quantity,
            'buying_price': self.buying_price,
            'selling_price': self.selling_price,
            'sales': self.sales,
            'sales_date': self.sales_date,
            'store_id': self.store_id
        }

    def calculate_revenue(self):
        return self.selling_price * self.stock_quantity

    def calculate_profit(self):
        return (self.selling_price - self.buying_price) * self.stock_quantity

    def __repr__(self):
        return f"Product(name='{self.name}', store_id='{self.store_id}')"

class PaymentStatus(Enum):
    NOT_PAID = 'Not Paid'
    PAID = 'Paid'

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Enum(PaymentStatus), default=PaymentStatus.NOT_PAID, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Integer)
    method = db.Column(db.String)
    due_date = db.Column(db.Date, nullable=True)

class Request(db.Model, SerializerMixin):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    requester_name = db.Column(db.String(100), nullable=True)
    requester_contact = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=True, default='Pending')

    @validates('quantity')
    def validate_quantity(self, key, quantity):
        assert quantity > 0, "Quantity must be a positive integer"
        return quantity
