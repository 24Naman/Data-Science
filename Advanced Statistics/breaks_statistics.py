#!/usr/bin/python

"""
    10-08-2018
    Author: Naman Jain

"""
import math

import numpy as np
import pandas as pd
from scipy import stats


def make_confidence_interval(breaks):
    """
        function to create confidence interval`
    :param breaks:
    :return: calculated confidence interval
    """
    # the size of sample
    sample_size = 100

    # a sample of sample_size taken from the 9000 breaks population from before
    # noinspection PyUnresolvedReferences
    sample = np.random.choice(a=breaks, size=sample_size)

    # the sample mean of the breaks lengths sample
    sample_mean = sample.mean()

    # sample standard deviation
    sample_std = sample.std()

    # population standard deviation estimate
    sigma = sample_std / math.sqrt(sample_size)

    confidence_interval = stats.t.interval(
        alpha=0.95,  # 95% confidence level
        df=sample_size - 1,  # degree of freedom
        loc=sample_mean,  # sample mean
        scale=sigma  # standard deviation
    )

    return confidence_interval


def main():
    """
        Main Function
    """
    # noinspection PyUnresolvedReferences
    np.random.seed(1234)

    # Office data set
    # represents the 3000 people who take about a 60 minute break
    long_breaks_in_company = stats.poisson.rvs(loc=10, mu=60, size=3000)

    # represents the 6000 people who take about a 15 minute break
    short_breaks_in_company = stats.poisson.rvs(loc=10, mu=15, size=6000)

    # put together the two arrays to get our "population" of 9000 people
    # noinspection PyUnresolvedReferences
    company_breaks = np.concatenate([short_breaks_in_company, long_breaks_in_company])

    # total average break length
    # 39.99 minutes is our parameter
    print(f"Break's Mean: {company_breaks.mean()}")

    # # Sampling Distribution
    print("Sampling Distribution")
    # sampling is important because it helps us to create normal distribution which would help us
    #  in doing all the calculation which can be performed on normal distribution

    # Bi-Modal Distribution
    pd.DataFrame(company_breaks).hist(bins=50, range=(5, 100))
    # plt.show()

    # # normalizing the sample data
    print("Normalizing the sampled data using point estimates")

    # POINT ESTIMATE
    # We take sample and use it to create point estimate (mean, median, SD, etc.)
    # then we create an interval around the sample mean
    point_estimates = []

    # generate 500 samples, each of size 100
    for x in range(500):
        print(f"Creating point estimate: {x}")
        # noinspection PyUnresolvedReferences
        sample = np.random.choice(a=company_breaks, size=100)
        # take a sample of 100 points from the data

        # add the mean of the extracted data to the list of point estimates
        print("Adding sample (sized 100) mean to the list of point estimates")
        point_estimates.append(sample.mean())

        # generated data will be normalized
        # ## following statement must be remain commented to avoid high memory usage
        # pd.DataFrame(point_estimates).hist()
        # plt.show()

    # # confidence interval
    print("Calculating the Confidence Interval")
    times_in_interval = 0

    for i in range(10000):
        interval = make_confidence_interval(company_breaks)
        if interval[0] <= 39.99 <= interval[1]:
            # if 39.99 falls in the interval
            times_in_interval += 1

        print(f"times_in_interval; Turn {i}: {times_in_interval}")

    print(f"Alpha is 95%; Times values are in interval: {times_in_interval / 10000}")

    # # One Sample t-tests
    # used to check whether a qualitative date differs significantly from another data set

    long_breaks_in_engineering = stats.poisson.rvs(loc=10, mu=55, size=100)

    short_breaks_in_engineering = stats.poisson.rvs(loc=10, mu=15, size=300)

    # noinspection PyUnresolvedReferences
    engineering_breaks = np.concatenate([long_breaks_in_engineering, short_breaks_in_engineering])

    print(f"Company's Break's Mean: {company_breaks.mean()}")
    print(f"Engineering Department's Break's Mean: {engineering_breaks.mean()}")

    # # One Sample t-test: to check whether there is a difference between the overall company
    # population's break times and break times of the employees in the engineering department
    # STEP-BY-STEP

    # I) Hypothesis ->
    # H0 -> the engineering department takes breaks the same as the company an the whole
    # Two-Tailed Test* ->
    # Ha -> The engineering department does not takes break the same as the company as the whole
    # One-Tailed Test ->
    # Ha -> The engineering department takes longer breaks
    # Ha -> The engineering department takes shorter breaks

    # II) Determine the sample size
    # It should be at least 30 points (it it 400 since we've generated it)
    # It should be less then 10% of the population (population_size = 900 (500 of company and 400
    #  of engineering))

    # III) Choose the significance level -> 95%; alpha is 1 - 0.95 = 0.05
    # IV) Collect the data -> Done

    # V) Decide whether to reject or fail to reject the null hypothesis

    t_statistic, p_value = stats.ttest_1samp(a=engineering_breaks, popmean=company_breaks.mean())

    print(f't_statistic = {round(t_statistic, 3)}, p_value = {round(p_value, 8)}, '
          f'significance_level = 1 - 0.95 = 0.05')


if __name__ == '__main__':
    main()
