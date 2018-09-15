#!/usr/bin/python

"""
    15-09-2018
    Author: Naman Jain

"""

import pandas as pd
from matplotlib.pyplot import show


def scatter_plots():
    """
        Create Scatter Plot
    """
    hours_tv_watched = [0, 0, 0, 1, 1.3, 1.4, 2, 2.1, 3.6, 3.2, 4.1, 4.4, 4.4, 5]

    # rating on work from 0 to 100
    work_performance = [87, 89, 92, 90, 82, 80, 77, 80, 76, 85, 80, 75, 73, 72]

    data_frame = pd.DataFrame(
        {'hours_tv_watched': hours_tv_watched,
         'work_performance': work_performance
         }
    )

    data_frame.plot(x='hours_tv_watched', y='work_performance', kind='scatter')
    show()

    data_frame.plot(x='hours_tv_watched', y='work_performance', kind='line')
    show()

    data_frame.plot(x='hours_tv_watched', y='work_performance', kind='bar')
    show()

    data_frame.plot(x='hours_tv_watched', y='work_performance', kind='scatter')
    show()


def main():
    """
        Main Function
    """
    scatter_plots()


if __name__ == '__main__':
    main()
