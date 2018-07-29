#!/usr/bin/python

"""
    04-06-2018
    Author: Naman Jain

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


# noinspection PyUnresolvedReferences
def main():
    """
        Main Function
    """
    np.random.seed(1234)

    # rvs generates variable with mean=mu and of size=size
    # loc is location parameter, it decide the the shift in the distribution

    # # distribution for people who take long break
    # represents 3000 people who take an average 60 minutes break
    long_breaks = stats.poisson.rvs(loc=10, mu=60, size=3000)

    pd.Series(long_breaks).hist()
    # plt.show()

    # # distribution for people who take short break
    # represents 3000 people who take an average 15 minutes break
    short_breaks = stats.poisson.rvs(loc=10, mu=15, size=6000)

    pd.Series(short_breaks).hist()
    # plt.show()

    breaks = np.concatenate((long_breaks, short_breaks))

    pd.Series(breaks).hist()
    # plt.show()

    # since asking each employee would be very difficult so will make a point estimate
    # taking sample of 100 people
    sample_breaks = np.random.choice(a=breaks, size=100)
    print(breaks.mean() - sample_breaks.mean())

    pd.DataFrame(breaks).hist(bins=50, range=(5, 100))
    # plt.show()

    # Sampling distributions

    point_estimates = []

    # generate 500 samples
    for x in range(500):
        # take a sample of 100 points
        sample = np.random.choice(a=breaks, size=100)
        # adding sample mean to out list of point estimates
        point_estimates.append(sample.mean())

    pd.DataFrame(point_estimates).hist()
    plt.show()


if __name__ == '__main__':
    main()
