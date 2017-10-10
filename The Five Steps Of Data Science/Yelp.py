#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 11-10-2017

"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    yelp_raw_data = pd.read_csv("../datasets/csv/misc/yelp.csv")

    print("First five rows -->")
    print(yelp_raw_data.head())

    # row and columns in data
    print("Shape of data: ", yelp_raw_data.shape)

    # description of dataframe
    print("Description of data frame", yelp_raw_data.describe(), sep="\n")

    # sorting the counts
    data = yelp_raw_data['stars'].value_counts()
    sorted_data = data.sort_values()

    # plotting the data
    plt.plot(sorted_data)
    plt.show()
