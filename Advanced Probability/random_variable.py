#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 01-05-2018
    File: random_variable

"""

import random

import matplotlib.pyplot as plt


def random_variable_of_dice_roll():
    """
        random variable of dice roll
    """

    # includes 1, 2, 3, 4, 5, 6
    return random.randint(1, 7)


def main():
    """
        Main Function
    """
    trials = []
    num_trials = 100
    for _ in range(num_trials):
        trials.append(random_variable_of_dice_roll())

    print(sum(trials)/float(num_trials))

    num_trials = range(100, 10000, 10)
    averages = []
    for num_trial in num_trials:
        trials = []
        for trial in range(1, num_trial):
            trials.append(random_variable_of_dice_roll())

        averages.append(sum(trials) / float(num_trial))

    plt.plot(num_trials, averages)
    plt.xlabel("Number of Trials")
    plt.ylabel("Average")

    plt.show()


if __name__ == '__main__':
    main()
