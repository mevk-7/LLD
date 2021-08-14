"""
This file contains code for coffee machine
"""

from src.main.inventory import Inventory
from concurrent.futures.thread import ThreadPoolExecutor
from src.main.logger import get_logger


class CoffeeMachine:

    """
    class for coffee machine
    """
    def __init__(self, slots):
        """
        constructor of the class
        :param slots: Number of slots
        """
        self.slots = slots
        self.logger = get_logger()
        self.inventory = Inventory(logger=self.logger)
        self.executor = ThreadPoolExecutor(max_workers=self.slots)
        self.supported_beverage = dict()

    def can_make_beverage(self, beverage):
        """
        check whether a beverage can be made using available ingredient
        :param beverage: beverage object
        :return: boolean value (True/False)
        """
        return self.inventory.check_availability(beverage.ingredients)

    def add_beverage(self, beverage_name, beverage):
        """
        add beverage to supported list
        whenever an order is placed it will first check
        whether beverage is supported by machine
        :param beverage_name: name of beverage
        :param beverage: beverage object
        :return: None
        """
        self.supported_beverage[beverage_name] = beverage

    def get_current_inventory(self):
        """
        Get the state of current inventory in form of dict('ingredient name': quantity)
        :return: dictionary
        """
        return self.inventory.get_current_inventory()

    def make_beverage(self, beverage_name):
        """
        make beverage based on beverage name
        :param beverage_name: name of beverage to make
        :return: boolean value , whether make is successful or not
        """
        if beverage_name not in self.supported_beverage:
            self.logger.info("{} is not available in the shop !!!".format(beverage_name))
            return False
        self.logger.info("Preparing beverage : {}".format(beverage_name))

        beverage = self.supported_beverage[beverage_name]

        if self.inventory.take_ingredient(beverage.ingredients):
            self.logger.info("{} is prepared ".format(beverage_name))
            return True
        self.logger.info("Currently we are out of stocks for {} !!!"
                         " Try another beverage".format(beverage_name))
        return False

    def place_order(self, beverage_name):
        """
        place order for beverage name , this function will spawn a thread for each order placed
        :param beverage_name: name of beverage
        :return: returns future object
        """

        return self.executor.submit(self.make_beverage, beverage_name)

    def refill_ingredient(self, ingredient_dict):
        """
        refill ingredients in inventory
        :param ingredient_dict: dictionary with key as
        ingredient and value as quantity
        :return: None
        """

        self.inventory.add_ingredients(ingredient_dict)





        






