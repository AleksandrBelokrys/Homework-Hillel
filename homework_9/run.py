from customer import Customer
from supplier import Supplier
from item import Item
from supply import Supply
from order import Order
from admin import Administrator
from review import Review

supply = list()
orders = list()
items = list()
reviews = list()

admin1 = Administrator("iamgod", "iamthelaw", "memyself@heavens.com")
supplier1 = Supplier("isupply", "4real", "Crab Shack Company", "Van Crabs",
                    "000-112-35-8", "crab@shack.biz")
supplier2 = Supplier("isupplytoo", "4real", "Reliable Company", "Van Reliable",
                    "011-112-35-8", "no-reply@reliable.biz")
customer1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                    "guido@python.org", "09-09-1968")
item1 = Item("Banana", "Better than ever before", 799.0,
            ("Golden", "Fresh Green"))
item2 = Item("Best Banana", "Better than others", 899.0,
            ("Truly Golden", "Fresher Green"))

customer1.add_review(item2, "very tasty", 5)
reviews.append(customer1.add_review(item2, "very tasty", 5))
print(reviews)
print(customer1.reviews[0].status)
print(admin1.approve_review(customer1.add_review(item2, "very tasty", 5)))



