from init import db, ma
from marshmallow import fields

class Order(db.Model):
    ''' Create order model'''

    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False)
    ship_date = db.Column(db.String, default='Not shipped', nullable=False)
    order_status_id = db.Column(db.Integer, db.ForeignKey("order_statues.id"), default=1, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    shipping_method_id = db.Column(db.Integer, db.ForeignKey("shipping_methods.id"), nullable=False)

    order_status = db.relationship('OrderStatus', back_populates='orders')
    customer = db.relationship('Customer', back_populates='orders')
    shipping_method = db.relationship('ShippingMethod', back_populates='orders')
    order_details = db.relationship('OrderDetail', back_populates='order', cascade='all, delete')



class OrderSchema(ma.Schema):
    user = fields.List(fields.Nested('UserSchema', only=['id']))
    address = fields.List(fields.Nested('AddressSchema', exclude=['customers']))
    shipping_method = fields.Nested('ShippingMethodSchema', exclude=['id'])
    order_details = fields.List(fields.Nested('OrderDetailSchema'))
    order_status = fields.Nested('OrderStatusSchema', exclude=['id'])


    
    class Meta:
        fields = ('id', 'order_date', 'ship_date', 'order_status', 'customer_id', 'shipping_method_id','shipping_method','order_details')
        ordered = True