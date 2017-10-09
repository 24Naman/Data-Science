#!/usr/bin/python


import pandas as pd

if __name__ == '__main__':
    yelp_raw_data = pd.read_csv("../datasets/csv/misc/yelp.csv")

    print("First five rows -->")
    print(yelp_raw_data.head())

    # row and columns in data
    print("Shape of data: ", yelp_raw_data.shape)

    # description of dataframe
    print("Description of data frame", yelp_raw_data.describe(), sep="\n")
