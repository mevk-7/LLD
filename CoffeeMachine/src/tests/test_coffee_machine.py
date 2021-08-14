from src.main.coffee_machine import CoffeeMachine
from src.main.beverage import Beverage
import json
import os
from concurrent import futures


def get_config():
    """
    get configuration from sample.json
    :return:
    """
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'sample.json')
    with open(json_path, 'r') as fp:
        obj = json.load(fp)
        return obj["machine"]


def get_machine():
    """
    create and return machine
    :return: instance of Coffee Machine
    """
    config = get_config()
    slots = config["outlets"]["count_n"]
    ingredient = config["total_items_quantity"]
    coffee_machine = CoffeeMachine(slots)
    coffee_machine.refill_ingredient(ingredient)

    beverages = config["beverages"]

    for beverage in beverages.keys():
        beverage_obj = Beverage(beverage, beverages[beverage])
        coffee_machine.add_beverage(beverage, beverage_obj)
    return coffee_machine


def get_inventory(state):
    """
    Get inventory state for testing
    :param state: state
    :return: dict
    """
    inventory_state = dict()

    inventory_state["first"] = get_config()["total_items_quantity"]
    inventory_state["second"] = {'hot_water': 200,
                                 'hot_milk': 0,
                                 'ginger_syrup': 60,
                                 'sugar_syrup': 40,
                                 'tea_leaves_syrup': 40}
    inventory_state["third"] = {'hot_water': 400,
                                 'hot_milk': 0,
                                 'ginger_syrup': 60,
                                 'sugar_syrup': 50,
                                 'tea_leaves_syrup': 40}
    inventory_state["fourth"] = {'hot_water': 100, 'hot_milk': 0,
                                 'ginger_syrup': 30, 'sugar_syrup': 50,
                                 "green_mixture": 30,
                                 'tea_leaves_syrup': 10,
                                 }

    return inventory_state[state]


def test_coffee_machine():
    """
    test coffee machine
    The Test contains
    1. Creation of coffee machine based on initial sample configuration
    2. Add supported beverage to machine
    3.1. Placing orders for beverage when it is possible to prepare it
    3.2. Placing orders for beverage when it is not possible to prepare
         based on ingredient available
    3.3 Placing orders for beverages which are not supported
    4. Refill the machine with ingredient
    5. Check the status of ingredient
    :return: None
    """

    coffee_machine = get_machine()
    t1 = coffee_machine.place_order("hot_tea")
    t2 = coffee_machine.place_order("hot_coffee")
    for future in futures.as_completed([t1, t2]):
        assert future.result() is True

    assert coffee_machine.get_current_inventory() == get_inventory("second")
    t3 = coffee_machine.place_order("black_tea")

    for future in futures.as_completed([t3]):
        assert future.result() is False
    coffee_machine.refill_ingredient({
        "sugar_syrup": 10,
        "hot_water": 200
    })

    assert coffee_machine.get_current_inventory() == get_inventory("third")

    t4 = coffee_machine.place_order("green_tea")
    invalid_beverage = coffee_machine.place_order("akfde")
    for future in futures.as_completed([t4, invalid_beverage]):
        assert future.result() is False
    t5 = coffee_machine.place_order("black_tea")

    for future in futures.as_completed([t5]):
        assert future.result() is True

    coffee_machine.refill_ingredient({
        "sugar_syrup": 50,
        "green_mixture": 30
    })
    assert coffee_machine.get_current_inventory() == get_inventory("fourth")

    t6 = coffee_machine.place_order("green_tea")
    for future in futures.as_completed([t6]):
        assert t6.result() is True


