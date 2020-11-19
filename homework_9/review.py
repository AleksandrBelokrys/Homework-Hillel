import uuid


class Review:
    def __init__(self, customer, item, text, rating):
        self.id = uuid.uuid4()
        self.customer = customer
        self.item = item
        self.text = text
        self.status = "Moderation"

        if isinstance(rating, int) and 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError('Rating must to be beetwen 1 and 5!')

    def __str__(self):
        return f"Review {self.id} \n{self.customer.username} -> {self.item.title}:\
             \n{self.text}, {self.rating} \n({self.status})"

    def __repr__(self):
        return f"{self.id}: {self.text}, {self.rating}"


if __name__ == '__main__':
    from customer import Customer
    from item import Item
    from admin import Administrator

    a1 = Administrator("iamgod", "iamthelaw", "memyself@heavens.com")
    c1 = Customer("iamguido", "4sure", "Guido", "Van Rossum", "000-112-35-8",
                  "guido@python.org", "09-09-1968")
    i1 = Item("Banana", "Better than ever before", 799.0,
              ("Golden", "Fresh Green"))
    r1 = Review(c1, i1, 'So delicious', 4)
    print(r1)

    a1.approve_review(r1)
    print(r1)

