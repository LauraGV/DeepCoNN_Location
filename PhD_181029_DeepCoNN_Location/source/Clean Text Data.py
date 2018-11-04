# coding: utf-8
import json
import pandas as pd
from keras.preprocessing.text import text_to_word_sequence

def clean(text):
    return text_to_word_sequence(text,
                                 filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
                                 lower=True, split=" ")
    
data = pd.read_csv("../data/hotelRevs.csv")

cleaned_text = data.loc[:, ["reviewerID", "asin", "overall", "reviewerCity", "reviewerProvince"]]
cleaned_text.loc[:, "reviewText"] = data.loc[:, "reviewText"].apply(clean)

cleaned_text.to_csv("../data/cleaned_reviews.csv")

