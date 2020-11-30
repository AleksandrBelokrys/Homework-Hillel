import uuid
from user import User
from order import Order
from review import Review
from logger import logger


class Customer(User):
    def __init__(self, username, userpass, first_name, last_name, phone,
                email, date_of_birth):
        super().__init__(username, userpass, email)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.bonus_amount = 0
        self.orders = list()
        self.reviews = list()
        logger.info(
            f"A customer '{self.first_name} {self.last_name}' was created.")

    def __str__(self):
        return f"Customer {self.id}: {self.username} ({self.first_name} {self.last_name})"

    def create_order(self, item, amount):
        new_order = Order(self, item, amount)
        self.orders.append(new_order)
        logger.info(
            f"An order of {amount} '{item.title}' has been created."
        )
        return new_order

    def add_review(self, item, text, rating):
        new_review = Review(self, item, text, rating)
        self.reviews.append(new_review)
        logger.info(
            f"{self.first_name} {self.last_name}'s review for '{item.title}' was added.")
        return new_review


if __name__ == '__main__':
    from item import Item

    c2 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                "guido@python.org", "09-09-1968")
    i1 = Item("Banana", "Better than ever before", 799.0,
                ("Golden", "Fresh Green"))
    c2.add_review(i1, "very tasty", 4)

    c2.create_order(i1, 4)
