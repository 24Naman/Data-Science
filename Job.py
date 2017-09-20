#!/usr/bin/python3

"""
    Grabbing data from web
"""
import requests  # for grabbing data from web

from bs4 import BeautifulSoup  # used to parse HTML
from sklearn.feature_extraction.text import CountVectorizer  # used to count num of words

TEXT = list()  # holding job description

for index in range(0, 1000, 10):
    # identify the url of the job listings
    page = 'http://indeed.com/jobs?q=data+scientist&start=' + str(index)

    web_results = requests.get(page).text  # visiting the url

    soup = BeautifulSoup(web_results)  # parse the html of the resulting page

    for listing in soup.findAll('span', {'class': 'summary'}):  # for each listing in the page
        TEXT.append(listing.text)

    type(TEXT)  # == list

    # Get basic counts of one and two word phrases
    vector = CountVectorizer(ngram_range=(1, 2), stop_words='english')

    # fit and learn to the vocabulary in the corpus
    matrix = vector.fit_transform(TEXT)

    # how many features are there
    print(vector.get_feature_names())
