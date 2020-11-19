import uuid
from user import User
from order import Order
from review import Review


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

    def __str__(self):
        return f"Customer {self.id}: {self.username} ({self.first_name} {self.last_name})"

    def create_order(self, item, amount):
        new_order = Order(self, item, amount)
        self.orders.append(new_order)
        return new_order

    def add_review(self, item, text, rating):
        new_review = Review(self, item, text, rating)
        self.reviews.append(new_review)
        return new_review


if __name__ == '__main__':
    from item import Item

    c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                "guido@python.org", "09-09-1968")
    i1 = Item("Banana", "Better than ever before", 799.0,
                ("Golden", "Fresh Green"))
    c1.create_order(i1, 3)
    print(c1)
    print(c1.orders)
    c1.add_review(i1, "very tasty", 4)
    print(c1.reviews)