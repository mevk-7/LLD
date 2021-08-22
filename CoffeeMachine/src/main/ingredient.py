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
        self._name = name
        self._quantity = quantity
        self._lock = RLock()
        self._timeout = 30  # 30 sec

    def get_quantity(self):
        """
        return: quantity available
        """
        return self._quantity

    def get_name(self):
        """
        return: name of ingredient
        """
        return self._name

    def use_ingredient(self, quantity):
        """
        subtract quantity to ingredient
        :param quantity: quantity to be subtracted by thread
        :return: boolean , whether the process is success
        """
        if quantity < 0:
            raise Exception("Cannot subtract quantity "
                            "= {}".format(quantity))
        self._lock.acquire(timeout=self._timeout)
        if self._quantity < quantity:
            self._lock.release()
            return False
        self._quantity -= quantity
        self._lock.release()
        return True

    def add_quantity(self, quantity):
        """
        add quantity to ingredient
        :param quantity : quantity added to
        """
        if quantity < 0:
            raise Exception("Cannot add negative quantity")
        self._lock.acquire(timeout=self._timeout)
        self._quantity += quantity
        self._lock.release()

