#!/usr/bin/python

"""
    15-09-2018
    Author: Naman Jain

"""

import matplotlib.pyplot as plt
import pandas as pd

DRINKS = pd.read_csv(r"D:\Naman\Data-Science\Rdatasets-master\Rdatasets-master\csv\Naman\drinks.csv")


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
    plt.show()

    data_frame.plot(x='hours_tv_watched', y='work_performance', kind='line')
    plt.show()

    data_frame.plot(x='hours_tv_watched', y='work_performance', kind='bar')
    plt.show()

    data_frame.plot(x='hours_tv_watched', y='work_performance', kind='hist')
    plt.show()


def bar_charts():
    """
    :return:
    """

    DRINKS.continent.value_counts().plot(kind="bar", title='Countries per continent',
                                         x='Continent', y="Count")
    plt.show()

    DRINKS.groupby('continent').beer_servings.mean().plot(kind='bar')
    plt.show()


def histograms():
    """

    :return
    """
    rossmann_sales = pd.read_csv(r"D:\Naman\Data-Science\Rdatasets-master\Rdatasets-master\csv"
                                 r"\Naman\rossmann.csv")
    print(rossmann_sales.head())

    # sub-setting the data only for the first store
    first_rossmann_sales = rossmann_sales[rossmann_sales['Store'] == 1]

    # plotting histogram
    first_rossmann_sales['Customers'].hist(bins=20)

    plt.xlabel('Customer Bins')
    plt.ylabel('Count')

    plt.show()


def box_plots():
    """
        Box Plots
    :return:
    """
    DRINKS.boxplot(column='beer_servings', by='continent')
    plt.show()

    DRINKS.boxplot(column='beer_servings', vert=False)
    plt.show()


def main():
    """
        Main Function
    """
    breakpoint()
    # scatter_plots()
    # bar_charts()
    # histograms()
    # box_plots()


if __name__ == '__main__':
    main()
