#!/usr/bin/python3

""""
    Standard deviation of Temperature
"""

import numpy
import math

# data of temperature
data = [31, 32, 32, 31, 28, 29, 31, 38, 32, 31, 30, 29, 30, 31, 26]

# mean
mean = numpy.mean(data)

# list for square of difference of data from mean
sqr_diff = list()

for i in data:
    sqr_diff.append((mean - i) ** 2)

avg = sum(sqr_diff) / len(sqr_diff)
SD = math.sqrt(avg)
print("Standard Deviation = ", SD)
