from ..models import *
from ..models.customer_order import CustomerOrder

session = Session()


def update_customer_order_controller(customer_id, data):
    received_id = customer_id
    received_name = data['name']
    received_address = data['address']
    received_barcode = data['barcode']
    received_price = data['price']
    received_amount = data['amount']
    received_explanation = data['explanation']
    db_data = session.query(CustomerOrder).filter_by(id=received_id).first()
    if db_data is not None:
        db_data.name = received_name
        db_data.address = received_address
        db_data.barcode = received_barcode
        db_data.price = received_price
        db_data.amount = received_amount
        db_data.explanation = received_explanation
        try:
            session.commit()
            return db_data.to_dict()
        except:
            return 400
    else:
        return 400
