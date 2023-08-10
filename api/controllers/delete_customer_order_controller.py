from ..models import *
from ..models.customer_order import CustomerOrder

session = Session()


def delete_customer_order_controller(data):
    received_id = data
    print(data)
    db_data = session.query(CustomerOrder).filter_by(id=received_id).first()
    print(db_data.to_dict())
    if db_data is not None:
        session.query(CustomerOrder).filter_by(id=received_id).delete()
        session.commit()
        return 200
    else:
        return []
