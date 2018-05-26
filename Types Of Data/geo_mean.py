#!/usr/bin/python3

"""
    Geometric Mean: The geometric mean is the average growth of an investment computed by
    multiplying n variables and then taking the n square root.  In other words, it is the average
    return of an investment over time, a metric used to evaluate the performance of an investment
    portfolio.
    **
    The arithmetic mean is relevant any time several quantities add together to produce a total.
    The arithmetic mean answers the question, "if all the quantities had the same value, what would
    that value have to be in order to achieve the same total?"
    In the same way, the geometric mean is relevant any time several quantities multiply together
    to produce a product. The geometric mean answers the question, "if all the quantities had the
    same value, what would that value have to be in order to achieve the same product?"
    **

    Formula of Geometric Mean = (Product of data) ^ (1 / [len of data])

    !! Product of data = GM ^ (len of data)

"""
from functools import reduce


def main():
    """
        Main Function
    :return:
    """
    # growth rate in percentage
    stock_growth_rate = [1, 2, 2, 2, 2, 9, 9, 9, 9]

    product = reduce(lambda x, y: x * y, stock_growth_rate)
    geometric_mean = product ** (1 / len(stock_growth_rate))

    print(f"Geometric Mean: {geometric_mean}")
    print(f"Calculated Product: {product}")
    print(f"Original Value: {geometric_mean ** len(stock_growth_rate)}")


if __name__ == '__main__':
    main()
