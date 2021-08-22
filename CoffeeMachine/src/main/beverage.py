"""
This file contains code for Beverage class
"""


class Beverage:

    """
    This class holds information about beverage
    """
    def __init__(self, name, ingredients={}):
        """
        constructor of class
        :param name: name of beverage
        :param ingredients: dictionary ('ingredient': quantity)
        """
        self.name = name
        self._ingredients = ingredients

    def get_ingredients(self):
        return self._ingredients








