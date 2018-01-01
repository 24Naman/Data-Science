#!/usr/bin/python3

import pandas as pd

"""
    World alcohol data
       
"""

LINK = "https://raw.githubusercontent.com/sinanuozdemir/principles_of_data_science" \
       "/master/data/chapter_2/drinks.csv"

DRINKS = pd.read_csv(LINK)
# printing first 5 rows of csv
print(DRINKS.head())

# printing first 5 rows of csv
print("Continent description", DRINKS['continent'].describe())

# quantitative column
print("Beer servings description", DRINKS['beer_servings'].describe())
