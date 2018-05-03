#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 02-05-2018
    File: standard_deviation_and_variance

    Example of Standard Deviation and Variance
"""
import math
from typing import Any, Union


def calculate_mean(data: dict) -> Union[Any, float]:
    """
        calculating mean
    :param data: data
    :type data: dict
    :return: mean of the data
    :rtype: Union[Any, float]
    """
    return sum(list(data.values())) / len(data)


def calculate_variance(data: dict, mean: int) -> float:
    """
        calculate variance
    :param data: data
    :type data: dict
    :param mean: mean of the data
    :type mean: int
    :return: variance of the data
    :rtype: float
    """
    return sum([(i - mean) ** 2 for i in data.values()]) / len(data)


def calculate_standard_deviation(data: dict, mean: int) -> float:
    """
        calculate Standard Deviation
    :param data: data
    :type data: dict
    :param mean: mean of the data
    :type mean: int
    :return: standard deviation of the data
    :rtype: float
    """
    return math.sqrt(calculate_variance(data, mean))


def main():
    """
        Main Function
    """
    data_x = {1: 3, 2: 4, 3: 4, 4: 5, 5: 6, 6: 8}
    data_y = {1: 1, 2: 2, 3: 4, 4: 5, 5: 7, 6: 11}

    mean_x = calculate_mean(data_x)
    mean_y = calculate_mean(data_y)

    print(f"Mean ->")
    print(f"x: {mean_x}")
    print(f"y: {mean_y}", end='\n' * 2)

    print(f"Standard Deviation ->")
    print(f"x: {round(calculate_standard_deviation(data_x, mean_x), 2)}")
    print(f"y: {round(calculate_standard_deviation(data_y, mean_y), 2)}", end='\n' * 2)

    print(f"Variance ->")
    print(f"x: {round(calculate_variance(data_x, mean_x), 2)}")
    print(f"y: {round(calculate_variance(data_y, mean_y), 2)}", end='\n' * 2)


if __name__ == '__main__':
    main()
