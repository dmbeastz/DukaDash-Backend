from flask_bcrypt import Bcrypt
from models import Merchant,MerchantStatus,EmployeesStatus,Clerk,Admin,Store,Payment,PaymentStatus,Product,Request
from datetime import datetime
from app import app


bcrypt = app(Bcrypt)

def main ():
    with app.app_context ():
        Merchant.query.delete()
        Clerk.query.delete()
        Admin.query.delete()
        Store.query.delete()
        Payment.query.delete()
        Product.query.delete()
        Request.query.delete()

        