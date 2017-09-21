#!/usr/bin/python3

"""
    Mean and median in numpy

"""

import numpy

results = list()

i = int()
while i >= 0:
    try:
        i = int(input())
        if i > 0:
            results.append(i)
    except ValueError:
        pass

sorted_result = sorted(results)
print(sorted_result)

print(numpy.mean(results))
print(numpy.median(results))
