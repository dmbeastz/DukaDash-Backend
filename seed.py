from flask_bcrypt import Bcrypt
from app import app
from models import Merchant, Store, Admin, Clerk, Product, Payment, PaymentStatus, Request, db, MerchantStatus, EmployeesStatus
from datetime import datetime

bcrypt = Bcrypt(app)

def main():
    with app.app_context():
        # Delete existing data
        Merchant.query.delete()
        Store.query.delete()
        Admin.query.delete()
        Clerk.query.delete()
        Product.query.delete()
        Payment.query.delete()
        Request.query.delete()

        # Seed Merchants
        merchants = [
            Merchant(
                name="Dave Roy Mutisya",
                username="MerchantDave",
                email="myduka7@gmail.com",
                password=bcrypt.generate_password_hash("Merchant1@pass").decode('utf-8'),
                image="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png",
                role = 'merchant',
                status = MerchantStatus.ONLINE
            ),
            Merchant(
                name="Alice Johnson",
                username="MerchantAlice",
                email="alice.johnson@example.com",
                password=bcrypt.generate_password_hash("Merchant2@pass").decode('utf-8'),
                image="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png",
                role = 'merchant',
                status = MerchantStatus.ONLINE
            )
        ]
        db.session.add_all(merchants)
        db.session.commit()

        # Seed Stores
        stores = [
            Store(name="Quickmart", image='https://i.pinimg.com/736x/eb/f6/b0/ebf6b0b574fd43fa3f742c8e8027a19c.jpg', location="Kilimani", merchant_id=1),
            Store(name="Naivas", image='https://i.pinimg.com/736x/5a/fc/41/5afc41b83e96ee1322c833045dcacc34.jpg', location="Thome", merchant_id=1),
            Store(name="Carrefour", image='https://i.pinimg.com/564x/8f/6a/0b/8f6a0bc9cddf0db6a8b138afda9f1945.jpg', location="Karen", merchant_id=2),
            Store(name="Best-Buy", image='https://i.pinimg.com/236x/7a/44/e3/7a44e3787ab159b6cb4131bd40801514.jpg', location="Lavington", merchant_id=2)
        ]
        db.session.add_all(stores)
        db.session.commit()

        # Seed Admins
        admins = [
            Admin(
                username="RonnieAdmin",
                name="Ronnie Langat",
                email="ronnie.langat@example.com",
                password=bcrypt.generate_password_hash("Admin1@pass").decode('utf-8'),
                store_id=1,
                image="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
            )
        ]
        db.session.add_all(admins)
        db.session.commit()

        # Seed Clerks
        clerks = [
            Clerk(
                username="TeddyClerk",
                name="Teddy Maina",
                email="teddy.maina@example.com",
                password=bcrypt.generate_password_hash("Clerk1@pass").decode('utf-8'),
                store_id=2,
                image="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
            ),
            Clerk(
                username="BrianClerk",
                name="Brian Murigi",
                email="brian.murigi@example.com",
                password=bcrypt.generate_password_hash("Clerk2@pass").decode('utf-8'),
                store_id=3,
                image="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
            )
        ]
        db.session.add_all(clerks)
        db.session.commit()

        # Seed Products
        products = [
            Product(name="Milk", price=70, stock_quantity=50, buying_price=600, selling_price=670, store_id=1, image="https://i0.wp.com/www.neokingshop.online/wp-content/uploads/2020/07/KCC-gold-crown-log-life-milk-carton.jpeg?fit=302%2C302&ssl=1", sales=10, sales_date=datetime.utcnow()),
            Product(name="Salt", price=90, stock_quantity=20, buying_price=90, selling_price=180, store_id=2, image="https://greenspoon.co.ke/wp-content/uploads/2023/10/Greenspoon-Kensalt-2Kg-1.jpg", sales=40, sales_date=datetime.utcnow()),
            Product(name="Bread", price=20, stock_quantity=70, buying_price=90, selling_price=120, store_id=3, image="https://www.beeqasi.co.ke/wp-content/uploads/2020/08/SUPERLOAF.jpeg", sales=30, sales_date=datetime.utcnow()),
            Product(name="Sugar", price=100, stock_quantity=50, buying_price=100, selling_price=120, store_id=4, image="https://i.pinimg.com/236x/0d/2f/98/0d2f9889b866218b70d201f75f144dfa.jpg", sales=50, sales_date=datetime.utcnow())
        ]
        db.session.add_all(products)
        db.session.commit()

        # Seed Payments
        payments = [
            Payment(store_id=1, product_name="Milk", status=PaymentStatus.PAID, amount=1000, method="Cash", due_date=datetime.strptime("2024-06-01", "%Y-%m-%d").date(), date=datetime.strptime("2024-05-20", "%Y-%m-%d").date()),
            Payment(store_id=2, product_name="Salt", status=PaymentStatus.NOT_PAID, amount=1500, method="Card", due_date=datetime.strptime("2024-06-05", "%Y-%m-%d").date(), date=datetime.strptime("2024-06-01", "%Y-%m-%d").date()),
            Payment(store_id=3, product_name="Bread", status=PaymentStatus.NOT_PAID, amount=2000, method="Cash", due_date=datetime.strptime("2024-06-07", "%Y-%m-%d").date(), date=datetime.strptime("2024-06-03", "%Y-%m-%d").date())
        ]
        db.session.add_all(payments)
        db.session.commit()

        # Seed Requests
        requests = [
            Request(store_id=1, product_name="Product A", quantity=10, requester_name="Victor Leyian", requester_contact="1234567890", status="Pending"),
            Request(store_id=2, product_name="Product B", quantity=15, requester_name="Teddy Maina", requester_contact="0987654321", status="Approved"),
            Request(store_id=3, product_name="Product C", quantity=20, requester_name="Brian Murigi", requester_contact="9876543210", status="Pending")
        ]
        db.session.add_all(requests)
        db.session.commit()

        print("Done seeding!")

if __name__ == "__main__":
    main()
