#!/usr/bin/python

"""
    30-05-2018
    Author: Naman Jain

"""

import pandas as pd


def main():
    """
        Main Function
    """
    friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485,
               1309, 472, 1132, 1773, 906, 531, 742, 621]

    happiness = [.8, .6, .3, .6, .6, .4, .8, .5, .4, .3, .3, .6, .2, .8, .1, .6, .2, .7, .5, .3,
                 .1, 0, .3, 1]

    data_frame = pd.DataFrame({'friends': friends, 'happiness': happiness})

    print(data_frame.head())


if __name__ == '__main__':
    main()
