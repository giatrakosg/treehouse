import pandas as pd
import numpy as np
import nltk
nltk.download('vader_lexicon')
from ExplicitMF import ExplicitMF
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def normalize(sent):
    if (sent<=1 and sent>=0.5):
        return 5
    elif (sent<0.5 and sent>0):
        return 4
    elif (sent==0):
        return 3
    elif (sent<0 and sent>=-0.5):
        return 2
    else:
        return 1


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

reviews = pd.read_csv('../data/reviews.csv')
listings = pd.read_csv('../data/listings.csv')

analyzer = SentimentIntensityAnalyzer()

reviews = reviews.dropna()

reviews['scores'] = reviews['comments'].apply(lambda x :analyzer.polarity_scores(x)['compound']).apply(normalize)

print(reviews.head())

#rec = ExplicitMF()
