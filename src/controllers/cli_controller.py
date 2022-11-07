from flask import Blueprint
from init import db,bcrypt
from datetime import date
from models.user import User
from models.postcode import Postcode
from models.category import Category
from models.order_status import OrderStatus
from models.shipping_method import ShippingMethod
from models.address import Address
from models.customer import Customer
from models.payment_account import PaymentAccount, PaymentAccountSchema
from models.order import Order
from models.product import Product
from models.order_detail import OrderDetail
from models.review import Review



db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            first_name='John',
            last_name='Cleese',
            password=bcrypt.generate_password_hash('123').decode('utf-8'),#originally hashing return hexadecimal, it is better to use utf8
            is_admin=True
        ),
        User(
            first_name='Pop',
            last_name='Mart',
            password=bcrypt.generate_password_hash('456').decode('utf-8')
        )
    ]
    db.session.add_all(users)
    db.session.commit()

    postcodes = [
        Postcode(
            postcode=3000,
            state='VIC'
        ),
        Postcode(
            postcode=2000,
            state='SYD'
        )
    ]
    db.session.add_all(postcodes)
    db.session.commit()

    categories = [
        Category(
            type='sticker sheet'
        ),
        Category(
            type='sticker flake'
        )
    ]
    db.session.add_all(categories)
    db.session.commit()

    order_statues = [
        OrderStatus(
            type='received'
        ),
        OrderStatus(
            type='shipped'
        )
    ]
    db.session.add_all(order_statues)
    db.session.commit()

    shipping_methods = [
        ShippingMethod(
            type='standard',
            price=2
        ),
        ShippingMethod(
            type='express',
            price=10
        )
    ]
    db.session.add_all(shipping_methods)
    db.session.commit()

    addresses = [
        Address(
            street_number=1,
            street_name='rose street',
            suburb='melbourne',
            postcode_id=3000
        ),
        Address(
            street_number=2,
            street_name='elizabeth avenue',
            suburb='sydney',
            postcode_id=2000
        )
    ]
    db.session.add_all(addresses)
    db.session.commit()

    customers = [
        Customer(
            email='popmart@spam.com',
            phone=1234565,
            user_id=2,
            address_id=1
        ),
    ]
    db.session.add_all(customers)
    db.session.commit()

    payment_accounts = [
        PaymentAccount(
            card_no = 1234567890,
            owner_name = 'John Cleese',
            expire_date = '12/01/2022',
            security_no = 500,
            encrypted_card_no = PaymentAccount.encrypt_card_no(1234567890),
            customer_id=1
        )
    ]
    db.session.add_all(payment_accounts)
    db.session.commit()

    orders = [
        Order(
            order_date=date.today(),
            ship_date=date.today(),
            order_status_id=1,
            customer_id=1,
            shipping_method_id=1
        ),
        Order(
            order_date=date.today(),
            ship_date=date.today(),
            order_status_id=2,
            customer_id=1,
            shipping_method_id=2
        )
    ]
    db.session.add_all(orders)
    db.session.commit()

    products = [
        Product(
            name='Payful PeterPan',
            description='Sticker sheet of peter pan',
            price=5.0,
            stock=10,
            create_date=date.today(),
            category_id=1
        ),
        Product(
            name='R U OK',
            price=3.0,
            stock=5,
            create_date=date.today(),
            category_id=2
        )
    ]
    db.session.add_all(products)
    db.session.commit()

    order_details = [
        OrderDetail(
            price=5.0,
            quantity=10,
            order_id=1,
            product_id=1
        ),
        OrderDetail(
            price=3.0,
            quantity=3,
            order_id=1,
            product_id=2
        ),
        OrderDetail(
            price=3.0,
            quantity=20,
            order_id=2,
            product_id=2
        )
    ]
    db.session.add_all(order_details)
    db.session.commit()

    reviews = [
        Review(
            comment='Love it!',
            rating=5,
            customer_id=1,
            product_id=1
        ),
        OrderDetail(
            price=3.0,
            quantity=3,
            order_id=1,
            product_id=2
        ),
        OrderDetail(
            price=3.0,
            quantity=20,
            order_id=2,
            product_id=2
        )
    ]
    db.session.add_all(reviews)
    db.session.commit()
# @db_commands.route('/')
# def get_all_payment_accounts():
#     stmt = db.select(PaymentAccount)
#     payment_account = db.session.scalar(stmt)
#     return PaymentAccountSchema().dump(payment_account)