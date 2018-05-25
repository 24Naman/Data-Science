#!/usr/bin/python3

"""
    Geometric Mean:

"""
from functools import reduce


def main():
    """
        Main Function
    :return:
    """
    # data of temperature
    data = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]

    product = reduce(lambda x, y: x * y, data)

    geo_mean = product ** (1 / len(data))

    print("Geometric Mean = ", geo_mean)


if __name__ == '__main__':
    main()
