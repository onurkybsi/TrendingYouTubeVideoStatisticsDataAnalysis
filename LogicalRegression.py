import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

processedDatas = pd.read_csv("processedDataset.csv")[["video_id","trending_date","title","channel_title","category","category_id","publish_time","tags","views","likes",
"dislikes","comment_count",
"comments_disabled","ratings_disabled","video_error_or_removed","country_abb", "views_scaled", "likes_scaled", "dislikes_scaled", "comment_count_scaled", "music_cat", 
"comedy_cat","entertainment_cat", "news&politics_cat", "people&blogs_cat", "howto&style_cat", "film&animation_cat", "science&technology_cat", "gaming_cat", "sports_cat",
"pets&animals_cat", "travel&events_cat", "autos&vehicles_cat", "education_cat", "shows_cat", "movies_cat", "trailers_cat", "ca_country", "de_country", "fr_country",
"gb_country", "in_country", "jp_country", "kr_country", "mx_country", "ru_country","us_country"
]]

pd.options.display.max_columns = None
pd.options.display.max_rows = None

# print(processedDatas.head(20))




# Logic regression
# Verilen view sayısına gore videonun entertainment kategorisine ait olup olmadığını buluyor.

entertainmentViewsPrediction = processedDatas[["views", "entertainment_cat"]]

X_train, X_test, y_train, y_test = train_test_split(entertainmentViewsPrediction[["views"]], entertainmentViewsPrediction.entertainment_cat, train_size=0.8)

model = LogisticRegression()

model.fit(X_train, y_train)

print(model.predict(X_test))
print(model.score(X_test, y_test))





# Random forest

