#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 13-10-2017

"""

import numpy as np

if __name__ == '__main__':
    # create user preferences
    user_pref = np.array([5, 1, 3])  # [comedy, romantic, action]

    # create a random movie matrix of 10,000 movies
    # it will random integers from (0-4) + 1 i.e. 1-5
    # size -> int or tuple of ints; if (m, n, k) then m * n * k samples is drawn
    # here the size of random matrix would be 3 * 10000
    movies = np.random.randint(5, size=(3, 10000)) + 1

    # print(f"User preferences array shape: {user_pref.shape}")
    # print(f"Movies rating array shape: {movies.shape}")

    # calculating dot matrix of user preferences array and movies array
    dot_matrix = np.dot(user_pref, movies)
    print(f"Dot matrix of user preferences and movie rating :-> {dot_matrix}")

    print(f"Index of the most recommended movie {np.argmax(dot_matrix)}")
    print(f"Index of the least recommended movie {np.argmin(dot_matrix)}")

