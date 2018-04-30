#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 27-04-2018
    File: Titanic.py

    Finding types of people who will likely to survive the disaster
"""

import pandas as pd


def main():
    """
        Main Function
    """
    sex, survived = 'Sex', 'Survived'
    titanic = pd.read_csv(r"../datasets/csv/Stat2Data/Titanic.csv")
    titanic = titanic[[sex, survived]]
    head = titanic.head()
    print(head)

    # finding probability of any given person is likely to survived
    # (no. of 1 in Survived column) / (total no. of records)
    num_rows = float(titanic.shape[0])
    p_survived = titanic[titanic.Survived == 1].sum()[survived] / num_rows
    p_not_survived = 1 - p_survived  # titanic[titanic.Survived == 0].sum()[survived] / num_rows

    # shape is (no. of rows, no. of columns)
    number_of_women = titanic[titanic.Sex == 'female'].shape[0]
    women_who_lived = titanic[(titanic.Sex == 'female') & (titanic.Survived == 1)].shape[0]

    print("Probabilities::")
    print(f"Survived: {p_survived}")
    print(f"Not Survived: {p_not_survived}")
    print(f"Number of women: {number_of_women}")
    print(f"Women who lived: {women_who_lived}")


if __name__ == '__main__':
    main()
