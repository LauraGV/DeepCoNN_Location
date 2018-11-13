import json
import pandas as pd
import math
from keras.preprocessing.text import text_to_word_sequence

def clean(text):
    print(text)
    if type(text)!=str:
        print("BINGO")
        return " "
    else:
        return text_to_word_sequence(text,
                                 filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
                                 lower=True, split=" ")
    
data = pd.read_csv("../data/Libro1.csv", encoding="ISO-8859-1")

#    asin    reviewer    country    overall    title    review
#cleaned_text = data.loc[:, ["reviewer", "asin", "overall", "country"]]
cleaned_text = data.loc[:, "reviewer"].apply(clean)
cleaned_text = data.loc[:, ["asin", "overall", "country"]]
cleaned_text.loc[:, "reviewText"] = (data.loc[:, "title"] + " " + data.loc[:, "review"]).apply(clean)

cleaned_text.to_csv("../data/cleaned_reviews02.csv")

