#!/usr/bin/python

"""
    28-05-2018
    Author: Naman Jain

"""
import numpy

import matplotlib.pyplot as plt


def main():
    """
        Main Function
    """
    # data of number of friends of 24 people on Facebook
    friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485,
               1309, 472, 1132, 1773, 906, 531, 742, 621]

    y_pos = range(len(friends))
    mean = int(numpy.mean(friends))

    plt.bar(y_pos, friends)
    plt.yticks(range(0, max(friends), 200))
    plt.plot((0, 25), (mean, mean), 'b-')     # mean
    plt.plot((0, 25), (mean + numpy.std(friends), mean + numpy.std(friends)), 'g-')   # mean + SD
    plt.plot((0, 25), (mean - numpy.std(friends), mean - numpy.std(friends)), 'r-')   # mean - SD

    plt.show()


if __name__ == '__main__':
    main()
