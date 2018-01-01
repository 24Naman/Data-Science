#!/usr/bin/python3

"""
    Mean and median in numpy

"""

import numpy

results = [5, 4, 3, 4, 5, 3, 2, 5, 3, 2, 1, 4, 5, 3, 4, 4, 5, 4, 2, 1, 4, 5, 4, 3, 2, 4, 4, 5, 4, 3, 2, 1]

sorted_result = sorted(results)
print(sorted_result)

print(numpy.mean(results))
print(numpy.median(results))
