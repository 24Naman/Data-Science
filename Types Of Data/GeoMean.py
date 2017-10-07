#!/usr/bin/python3

"""
    Geometric Mean

"""
from functools import reduce


if __name__ == '__main__':
    # data of temperature
    data = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]

    product = reduce(lambda x, y: x * y, data)

    geo_mean = product ** (1 / len(data))

    print("Geo Mean = ", geo_mean)
