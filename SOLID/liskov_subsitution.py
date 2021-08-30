"""
Now the code in open_for_extension_close_for_modification.py handles
Single responsibility and open closed principle but it violates
liskov substitution principle Base type PaymentProcessor has
method pay where we are passing secrete code to DebitPaymentProcessor and
CreditPaymentProcessor but in PayPalPaymentProcessor we are passing email id
hence PayPalPaymentProcessor is not replaceable by other sub type of PaymentProcessor

Here we are setting secret code / email id in construction hence making all inherited method
having same signature and replaceable
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
    def pay(self, total: float, order: Order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, secret_code: str) -> None:
        self.secret = secret_code

    def pay(self, total: float, order: Order) -> None:
        print(f"Authenticating secret code {self.secret}")
        print(f"payment done in debit mode amount : {total}")
        order.status = True


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, secret_code: str) -> None:
        self.secret = secret_code

    def pay(self, total: float, order: Order) -> None:
        print(f"Authenticating secret code {self.secret}")
        print(f"payment done in debit mode amount : {total}")
        order.status = True


class PayPalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_id: str) -> None:
        self.email_id = email_id

    def pay(self, total : float, order: Order) -> None:
        print(f"Authenticating using  email id {self.email_id}")
        print(f"payment done in paypal mode amount : {total}")
        order.status = True


if __name__ == '__main__':
    order_ = Order()
    order_.add_items("Apple Iphone 12", 1, 56000)
    order_.add_items("Mackbook M1 Air", 2, 120000)
    payment_processor = PayPalPaymentProcessor("h@gmail.com")
    payment_processor.pay(order_.get_total(), order_)

