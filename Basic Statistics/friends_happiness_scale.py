#!/usr/bin/python

"""
    30-05-2018
    Author: Naman Jain

"""

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing


def main():
    """
        Main Function
    """
    friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485,
               1309, 472, 1132, 1773, 906, 531, 742, 621]

    happiness = [.8, .6, .3, .6, .6, .4, .8, .5, .4, .3, .3, .6, .2, .8, .1, .6, .2, .7, .5, .3,
                 .1, 0, .3, 1]

    data_frame = pd.DataFrame({'friends': friends, 'happiness': happiness})

    print("Data w/o scaling: ")
    print(data_frame.head())

    print("Data with scaling: ")
    # the preprocessing module is used for revealing z-score of each column
    # it includes 1) finding mean 2) finding SD 3) applying z-score to each element
    data_frame_scaled = pd.DataFrame(preprocessing.scale(data_frame), columns=['friends_scaled',
                                                                               'happiness_scaled'])

    print(data_frame_scaled.head())

    data_frame_scaled.plot(kind='scatter', x='friends_scaled', y='happiness_scaled')

    plt.show()

    # correlation
    print(data_frame_scaled.corr())


if __name__ == '__main__':
    main()
