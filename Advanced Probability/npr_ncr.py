#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 04-05-2018
    File: npr_ncp

"""
from math import factorial


def npr(n, r) -> float:
    """
        calculating permutation
    :param n:
    :type n:
    :param r:
    :type r:
    """
    return factorial(n) / factorial(n - r)


def ncr(n, r) -> float:
    """
        calculating permutation
    :param n:
    :type n:
    :param r:
    :type r:
    """
    return factorial(n) / (factorial(r) * factorial(n - r))


def main():
    """
        Main Function
    """
    print(npr(5, 3))
    print(ncr(5, 3))


if __name__ == '__main__':
    main()
