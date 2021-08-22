"""
This file contains code for Inventory class
"""
from src.main.ingredient import Ingredient


class Inventory:
    """
    Inventory class
    """
    def __init__(self, logger):

        self.ingredients = dict()
        self.logger = logger

    def get_current_inventory(self):
        """
        :return: This function returns current state of inventory in
        form of dict ('ingredient': quantity)
        """

        available_ingredient = {}
        for ingredient in self.ingredients:
            available_ingredient[ingredient] = self.ingredients[ingredient].quantity

        return available_ingredient

    def add_ingredients(self, total_items_quantity):
        """
        add ingredients to inventory
        :param total_items_quantity: dict type where key is
        ingredient name and value is its quantity
        :return: None
        """
        for item in total_items_quantity.keys():
            quantity = total_items_quantity[item]
            if item in self.ingredients:
                self.ingredients[item].add_quantity(quantity)
            else:
                ingredient = Ingredient(item, quantity)
                self.ingredients[item] = ingredient

    def check_availability(self, ingredients_list):
        """
        this function checks availability of ingredient provided
        dict of ingredient where key is ingredient name and value
        is quantity required
        :param ingredients_list: list of ingredients
        :return: Boolean value whether all ingredient available or not
        """
        for ingredient in ingredients_list:
            ingredient_name = ingredient.name
            if ingredient_name in self.ingredients \
                    and self.ingredients[ingredient_name].quantity < ingredient.quantity:
                return False
            elif ingredient_name not in self.ingredients:
                return False
        return True

    def take_ingredient(self, ingredients_dict):
        """
        deduct ingredient from inventory
        take_ingredient is like transaction , either you commit or rollback
        :param ingredients_dict: dictionary where key is ingredient name and
        value is quantity required(will be deducted if transaction is committed)
        :return: boolean whether the whole process completed
        """
        ingredient_used = {}
        is_possible = True
        for ingredient_name in ingredients_dict.keys():
            quantity = ingredients_dict[ingredient_name]
            if ingredient_name in self.ingredients and \
                    self.ingredients[ingredient_name].use_ingredient(quantity):
                ingredient_used[ingredient_name] = quantity
            else:
                is_possible = False
                break

        # Commit
        if is_possible:
            return True

        # Rollback
        for ingredient in ingredient_used.keys():
            self.ingredients[ingredient].add_quantity(ingredient_used[ingredient])
        return False


