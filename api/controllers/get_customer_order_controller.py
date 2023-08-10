from ..models import *
from ..models.customer_order import CustomerOrder

session = Session()


def get_customer_order_controller(data):
    print(data,"dataa")
    received_id = data
    db_data = session.query(CustomerOrder).filter_by(id=received_id).all()
    result_list = list()
    for i in db_data:
        result_list.append(i.to_dict())
    if db_data is not None:
        session.commit()
        return result_list
    else:
        return []
