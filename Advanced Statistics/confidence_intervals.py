#!/usr/bin/python

"""
    28-06-2018
    Author: Naman Jain

"""
import math

import numpy as np
import pandas as pd
from scipy import stats


def main():
    """
        Main Function
    """
    long_breaks = stats.poisson.rvs(loc=10, mu=60, size=3000)

    pd.Series(long_breaks).hist()
    # plt.show()

    # # distribution for people who take short break
    # represents 3000 people who take an average 15 minutes break
    short_breaks = stats.poisson.rvs(loc=10, mu=15, size=6000)

    pd.Series(short_breaks).hist()
    # plt.show()

    breaks = np.concatenate((long_breaks, short_breaks))

    # ## Confidence Intervals ## #

    sample_size = 100

    sample = np.random.choice(a=breaks, size=sample_size)

    sample_mean = sample.mean()

    sample_std_dev = sample.std()

    # population standard deviation estimate
    sigma = sample_std_dev / math.sqrt(sample_size)

    interval = stats.t.interval(alpha=0.95,     # confidence level
                                df=sample_size - 1,     # degree of freedom
                                loc=sample_mean,    # location parameter (array-like)
                                scale=sigma     # scale parameter
                                )

    interval_mean = np.mean(interval)

    breakpoint()

    print("Confidence Interval: ", interval)
    print("Sample Mean: ", sample_mean)
    print("Interval Mean: ", interval_mean)


if __name__ == '__main__':
    main()
