#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 13-10-2017

    Law of large numbers -> if we repeat a procedure over and over,
    the relative frequency probability will approach the actual probability

    Calculating mean of random number between 1 to 10
"""

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

if __name__ == '__main__':
    # the 'result' will hold mean of 1, 2, 3, 4, ... 9999 numbers
    result = list()

    for n in range(1, 10000):
        # choose n numbers from 1 to 10
        nums = np.random.randint(low=1, high=10, size=n)

        # calculating mean of 1, 2, 3, 4 ... 9999 random numbers and adding to the list
        mean = nums.mean()
        result.append(mean)

    df = pd.DataFrame({'means': result})

    # the average in the beginning are all over the place
    print(df.head())

    # as size of data increases the average get close to 5
    print(df.tail())

    print(df['means'].mean())       # == actual mean (almost)

    # plotting the data
    df.plot(title="Law of Large Numbers")
    plt.xlabel("Number of throws in sample")
    plt.ylabel("Average of Sample")
    plt.show()
