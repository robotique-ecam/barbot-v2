#!/usr/bin/env python3

import bottles as bt


class Drink:
    def __init__(self, main_window, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.mainwindow = main_window

    def select_drink(self, drink_button):
        


water = Drink("Water", {bt.WATER: 100})
