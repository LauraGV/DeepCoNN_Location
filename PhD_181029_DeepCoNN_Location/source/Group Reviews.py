import json
import pandas as pd
import numpy as np
from time import time


#    asin    reviewer    country    overall    title    review
data = pd.read_csv("../data/cleaned_reviews.csv").drop("Unnamed: 0", axis=1)

def add_user_reviews(x):
    ur = user_reviews.loc[x["reviewer"]].drop(x["asin"]).values.tolist()
    mr = movie_reviews.loc[x["asin"]].drop(x["reviewer"]).values.tolist()
    x["userReviews"] = " ".join(list(map(lambda x: str(x[0]), ur)))
    x["movieReviews"] = " ".join(list(map(lambda x: str(x[0]), mr)))
    return x


user_item_review = data.drop("reviewText", axis=1)
user_reviews = pd.pivot_table(data,
                              index=["reviewer", "asin"],
                              aggfunc=lambda x: x).drop("overall", axis=1)
    
movie_reviews = pd.pivot_table(data,
                               index=["asin", "reviewer"],
                               aggfunc=lambda x: x).drop("overall", axis=1)



s = pd.Timestamp(int(time()), unit="s")
grouped_cleaned_data = user_item_review.apply(add_user_reviews, axis=1)
e = pd.Timestamp(int(time()), unit="s")
print("took {}".format(e - s))


grouped_cleaned_data.to_csv("../data/unembedded_grouped_cleaned_data.csv")

