#!/usr/bin/python3

"""
    World alcohol data

"""

import pandas as pd


def main():
    """
        Main Function
    """

    link = "https://raw.githubusercontent.com/sinanuozdemir/principles_of_data_science" \
           "/master/data/chapter_2/drinks.csv"

    drinks = pd.read_csv(link)
    # printing first 5 rows of csv
    print(drinks.head())

    # printing first 5 rows of csv
    print("Continent description", drinks['continent'].describe())

    # quantitative column
    print("Beer servings description", drinks['beer_servings'].describe())
