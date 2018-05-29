#!/usr/bin/python

"""
    30-05-2018
    Author: Naman Jain

"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    """
        Main Function
    """
    friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485,
               1309, 472, 1132, 1773, 906, 531, 742, 621]

    z_scores = []
    y_pos = range(len(friends))

    # average friends on facebook
    mean = np.mean(friends)
    std = np.std(friends)

    for friend in friends:
        # z scores
        z = (friend - mean) / std
        z_scores.append(z)

    # plot of z scores
    plt.bar(y_pos, z_scores)

    # plot at mean
    plt.plot((0, 25), (1, 1), 'g-')
    # plot at mean + SD
    plt.plot((0, 25), (0, 0), 'b-')
    # plot at mean - SD
    plt.plot((0, 25), (-1, -1), 'r-')

    plt.show()


if __name__ == '__main__':
    main()
