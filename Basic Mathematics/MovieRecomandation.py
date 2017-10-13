#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 13-10-2017

    Movie Recommendation system demo
"""

import numpy as np

if __name__ == '__main__':
    # create user preferences
    USER_PREF = np.array([5, 1, 3])  # [comedy, romantic, action]

    # create a random movie matrix of 10,000 movies
    # it will contain random integers from (0-4) + 1 i.e. 1-5
    # size -> int or tuple of ints; if (m, n, k) then m * n * k samples is drawn
    # here the size of random matrix would be 3 * 10000
    MOVIES = np.random.randint(5, size=(3, 10000)) + 1

    # print(f"User preferences array shape: {user_pref.shape}")
    # print(f"Movies rating array shape: {movies.shape}")

    # calculating dot matrix of user preferences array and movies array
    DOT_MATRIX = np.dot(USER_PREF, MOVIES)
    print(f"Dot matrix of user preferences and movie rating :-> {DOT_MATRIX}")

    print(f"Index of the most recommended movie {np.argmax(DOT_MATRIX)}")
    print(f"Index of the least recommended movie {np.argmin(DOT_MATRIX)}")
