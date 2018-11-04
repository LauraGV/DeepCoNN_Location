# coding: utf-8

# In[ ]:


import json
import pandas as pd
from keras.preprocessing.text import text_to_word_sequence

#open for reading text. Devuelve todo el fichero cargado en json
#def get_list_of_dicts(fname): return [csv.loads(i) for i in open(fname, "rt")]
#def get_list_of_dicts(fname): return pd.read_csv(fname)

def add_user_reviews(x):
    ur = user_reviews.loc[x["reviewerID"]].drop(x["asin"])
    mr = movie_reviews.loc[x["asin"]].drop(x["reviewerID"])
    x["userReviews"] = ur["reviewText"].tolist()
    x["movieReviews"] = mr["reviewText"].tolist()
    return x


def clean(text):
    return text_to_word_sequence(text,
                                 filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
                                 lower=True, split=" ")


#raw_data = get_list_of_dicts("../data/hotelRevs.csv")
'''
#data = pd.DataFrame(raw_data).loc[:,
                                  ["reviewerID",
                                   "reviewText",
                                   "asin",
                                   "overall"]]
'''
    
data = pd.read_csv("../data/hotelRevs.csv")
# In[ ]:


cleaned_text = data.loc[:, ["reviewerID", "asin", "overall", "reviewerCity", "reviewerProvince"]]
cleaned_text.loc[:, "reviewText"] = data.loc[:, "reviewText"].apply(clean)


# In[ ]:


cleaned_text.to_csv("../data/cleaned_reviews.csv")

