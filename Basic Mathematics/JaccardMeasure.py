#!/usr/bin/python3

"""
    Data-Science: Created by Naman Jain on 13-10-2017

"""

user1 = {"Target", "Banana Republic", "Old Navy"}
user2 = {"Banana Republic", "Gap", "Kohl's"}


def jaccard(user_1, user_2):
    stores_in_common = len(user_1 & user_2)
    stores_all_together = len(user_1 | user_2)

    return stores_in_common / float(stores_all_together)


if __name__ == '__main__':
    print(jaccard(user1, user2))
