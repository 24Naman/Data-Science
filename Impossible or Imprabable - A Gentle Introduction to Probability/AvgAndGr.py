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


def main():
    """
        Main function
    """
    # the 'result' will hold mean of 1, 2, 3, 4, ... 9999 numbers
    result = list()

    for size in range(1, 10000):
        # choose n numbers from 1 to 10
        nums = np.random.randint(low=1, high=10, size=size)
        # calculating mean of 1, 2, 3, 4 ... 9999 random numbers and adding to the list
        result.append(nums.mean())

    data_frame = pd.DataFrame({'means': result})

    # the average in the beginning are all over the place
    print(data_frame.head())

    # as size of data increases the average get close to 5
    print(data_frame.tail())

    print(data_frame['means'].mean())  # == actual mean (almost)

    # plotting the data
    data_frame.plot(title="Law of Large Numbers")
    plt.xlabel("Number of throws in sample")
    plt.ylabel("Average of Sample")
    plt.show()


if __name__ == '__main__':
    main()
