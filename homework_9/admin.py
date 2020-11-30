import uuid
from user import User
from logger import logger


class Administrator(User):
    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()

    def approve_review(self, review):
        review.status = "Published"
        logger.info(
            f"Status of review '{review.text}' has been changed to 'published'.")
        return review

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)

    def check_order(self, order):
        print(f"Checking order {order.id}")
        if not order.status == 'New':
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                logger.info(
                    f"Status of '{order}' has been changed to 'confirmed'.")
                return order
        order.status = 'On hold'
        logger.info(f"Status of '{order}' has been changed to 'on hold'.")
        return order
