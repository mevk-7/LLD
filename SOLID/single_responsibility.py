""""
Single responsibility principle says that a class
should have one and only one reason to change

Following class is example of bad design
This class has two responsibility 1. add and track order 2. make payment
This class will break if we add more payment method
One more important thing here is both responsibility are not of similar type
"""
from typing import List


class Order:

    items = []
    quantities = []
    prices = []
    status = False

    def add_items(self, name: str, quantity: float , price: float) -> None:

        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def get_total(self) -> float:
        total = 0
        for quantity, price  in zip(self.quantities, self.prices):
            total += quantity * price
        return total

    def process_order(self, payment_mode: str) -> None:
        total = self.get_total()
        if payment_mode == "cash":
            print(f"Payment done through cash with total amount {total} !!!!")
        elif payment_mode == "debit":
            print(f"Payment is done through debit card with total amount {total} !!!!")
        else:
            raise Exception("Payment method not supported !!")
        self.status = True


if __name__ == '__main__':
    order = Order()
    order.add_items("Apple Iphone 12", 1, 56000)
    order.add_items("Mackbook M1 Air", 2, 120000)
    order.process_order("cash")





