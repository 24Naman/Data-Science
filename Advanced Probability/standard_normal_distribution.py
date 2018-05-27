#!/usr/bin/python3

"""
    28-05-2018
    Author: Naman Jain

"""

import matplotlib.pyplot as plt
import numpy as np


def normal_pdf(x, mu=0, sigma=1):
    return (1. / np.sqrt(2 * 3.14 * sigma ** 2)) * 2.718 ** (-(x - mu) ** 2 / (2. * sigma ** 2))


def main():
    """
        Main Function
    """
    # Return evenly spaced numbers over a specified interval.
    # num is number of samples to be generated
    x_values = np.linspace(start=-5, stop=5, num=100)
    y_values = [normal_pdf(x) for x in x_values]

    plt.plot(x_values, y_values)
    plt.show()

    # with mu = 5
    y_values = [normal_pdf(x, mu=5) for x in x_values]

    plt.plot(x_values, y_values)
    plt.show()

    # with sigma = 5
    y_values = [normal_pdf(x, sigma=5) for x in x_values]

    plt.plot(x_values, y_values)
    plt.show()

    # with mu = 5 and sigma = 5
    y_values = [normal_pdf(x, mu=5, sigma=5) for x in x_values]

    plt.plot(x_values, y_values)
    plt.show()


if __name__ == '__main__':
    main()
