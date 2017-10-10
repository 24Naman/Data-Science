#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 10-10-2017

    The data is red and the null values are replaced by the mean value of their column
"""
import numpy as np
import pandas as pd

titanic = pd.read_csv(r"D:\Naman\Data-Science\datasets\csv\Stat2Data\Titanic.csv")
print(f"First five records: {titanic.head()}")
print(f"Shape of dataset: {titanic.shape}")

titanic['Sex'] = np.where(titanic['Sex'] == 'female', [1], [0])

print("Number of null values: ")
print(titanic.isnull().sum())

# calculating mean age
average_age = titanic['Age'].mean()

# replacing null values with average age
titanic['Age'].fillna(average_age, inplace=True)

print("Number of null values ->", titanic.isnull().sum(), sep='\n')

# average age by gender
avg_age_by_gender = titanic.groupby('Sex')['Age'].mean()
print(f"Average age of Female: {avg_age_by_gender[0]} and Male: {avg_age_by_gender[1]}")
