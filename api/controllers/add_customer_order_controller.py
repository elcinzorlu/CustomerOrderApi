from ..models import *
from ..models.customer_order import CustomerOrder

session = Session()


def add_customer_order_controller(data):
    try:
        new_customer_order = CustomerOrder(**data)
        session.add(new_customer_order)
        session.commit()
        return 200
    except Exception:
        return 400
