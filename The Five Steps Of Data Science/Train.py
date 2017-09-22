#!/usr/bin/python3

"""
    Analyzing train data using Python Pandas

"""

import pandas as pd

train_data = pd.read_csv("datasets/train.csv")

print(train_data.head())    # printing first five records

# shape of dataset
print(train_data.shape)   # num: (row, columns)

# type of dataset
print(type(train_data))     # pandas.core.frame.DataFrame

# grabbing single column
print(train_data['PassengerId'])    # pandas.core.series.Series

# describing the column (Qualitative Column)
print("PassengerId column", train_data['PassengerId'].describe())     # quick stats of column "PassengerId"

# describing the column (Qualitative Column)
print("Fare column", train_data['Fare'].describe())     # quick stats of column "Fare"
