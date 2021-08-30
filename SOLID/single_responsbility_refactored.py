"""
This file contain refactor code of single_responsibility.py

"""


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


class PaymentProcessor:
    @staticmethod
    def pay(order: Order, payment_mode: str,  total: float) -> None:
        if payment_mode == "cash":
            print(f"Payment done through cash with total amount {total} !!!!")
        elif payment_mode == "debit":
            print(f"Payment is done through debit card with total amount {total} !!!!")
        order.status = True


if __name__ == '__main__':
    order = Order()
    order.add_items("Apple Iphone 12", 1, 56000)
    order.add_items("Mackbook M1 Air", 2, 120000)
    payment_processor = PaymentProcessor()
    payment_processor.pay(order, "cash", order.get_total())
