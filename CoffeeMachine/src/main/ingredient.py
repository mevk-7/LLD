"""
This file contains code for ingredient clas
"""

from threading import RLock


class Ingredient:
    """
    class for Ingredient
    Key thing to note here is for each ingredient object
    one lock will be assign , at a time only one thread will be
    able to access the ingredient
    """
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.lock = RLock()
        self.timeout = 30  # 30 sec

    def use_ingredient(self, quantity):
        """
        subtract quantity to ingredient
        :param quantity: quantity to be subtracted by thread
        :return: boolean , whether the process is success
        """
        if quantity < 0:
            raise Exception("Cannot subtract quantity "
                            "= {}".format(quantity))
        self.lock.acquire(timeout=self.timeout)
        if self.quantity < quantity:
            self.lock.release()
            return False
        self.quantity -= quantity
        self.lock.release()
        return True

    def add_quantity(self, quantity):
        """
        add quantity to ingredient
        :param quantity : quantity added to
        """
        if quantity < 0:
            raise Exception("Cannot add negative quantity")
        self.lock.acquire(timeout=self.timeout)
        self.quantity += quantity
        self.lock.release()

