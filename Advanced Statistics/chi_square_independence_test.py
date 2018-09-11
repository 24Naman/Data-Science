#!/usr/bin/python

"""
    10-09-2018
    Author: Naman Jain

"""
from typing import Tuple, Union, Any

import numpy as np
from scipy import stats

OBSERVED = np.array([
    [136, 7], [55, 9], [239, 24]
])


def cal_chi_auto() -> Tuple[float, float, int, np.ndarray]:
    """
        calculating chi square manually
        :rtype: int
    """
    local_obs = np.copy(OBSERVED)
    local_obs = np.array(
        [[[i - j, j] for i, j in local_obs]]
    )
    return stats.chi2_contingency(observed=local_obs)


def cal_chi_man() -> Tuple[Union[int, Any], Union[int, Any]]:
    """
        calculating chi square manually
    """
    local_obs = np.copy(OBSERVED)
    local_obs = np.array(
        [[i - j, j] for i, j in local_obs]
    )

    expected_frequency = np.ndarray(local_obs.shape)

    col_sum, row_sum = local_obs.sum(axis=0), local_obs.sum(axis=1)

    # for calculating the expected frequency
    for row_index, row in enumerate(local_obs):
        for col_index, _ in enumerate(row):
            expected_frequency[row_index, col_index] = round(
                (row_sum[row_index] * col_sum[col_index]) / local_obs.sum(), 2
            )

    chi_value = sum(
        [
            (a - b) ** 2 / b
            for a, b in zip(local_obs.flatten(), expected_frequency.flatten())
        ]
    )

    degree_of_freedom = local_obs.shape[0] - 1 * local_obs.shape[1] - 1
    return chi_value, degree_of_freedom


def main():
    """
        Main Function
    """
    chi_squared, p_value, degrees_of_freedom, matrix = cal_chi_auto()
    print(f"Chi-Square value: {chi_squared}, P-Value: {p_value}, "
          f"Degrees of Freedom: {degrees_of_freedom}")

    chi_squared, degree_of_freedom = cal_chi_man()
    print(f"Chi-Square value: {chi_squared}, Degrees of Freedom: {degrees_of_freedom}")


if __name__ == '__main__':
    main()
