"""
Now the code in single_responsibility_refactored.py handles
Single responsibility but the class PaymentProcessor is not
correct , if want to add another method we have to modify
pre existing code
Better approach will be to create small classes to handle
most of the functionality
"""

from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = False

    def add_items(self, name: str, quantity: float, price: float) -> None:

        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def get_total(self) -> float:
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, total: float, order: Order, secret_code: str) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def pay(self, total: float, order: Order, secret_code: str) -> None:
        print(f"Authenticating secret code {secret_code}")
        print(f"payment done in debit mode amount : {total}")
        order.status = True


class CreditPaymentProcessor(PaymentProcessor):

    def pay(self, total: float, order: Order, secret_code: str) -> None:
        print(f"Authenticating secret code {secret_code}")
        print(f"payment done in debit mode amount : {total}")
        order.status = True


class PayPalPaymentProcessor(PaymentProcessor):

    def pay(self, total : float, order: Order, secret_code: str) -> None:
        print(f"Authenticating using  email id {secret_code}")
        print(f"payment done in paypal mode amount : {total}")
        order.status = True


if __name__ == '__main__':
    order_ = Order()
    order_.add_items("Apple Iphone 12", 1, 56000)
    order_.add_items("Mackbook M1 Air", 2, 120000)
    payment_processor = PayPalPaymentProcessor()
    payment_processor.pay(order_.get_total(), order_, "h@gmail.com")