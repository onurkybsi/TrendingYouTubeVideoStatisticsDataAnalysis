import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sn
import re



dataWarehouse = pd.read_csv("arrangedDataset.csv")[["video_id","trending_date","title","channel_title","category","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","country_abb"]]


# print(len(dataWarehouse[dataWarehouse["category"] == "Movies"] ))
# print(len(dataWarehouse[dataWarehouse["category"] == "Shows"] ))
# print(len(dataWarehouse[dataWarehouse["category"] == "Trailers"] ))
# print(dataWarehouse.category.unique())


# categoryCount = []

# for x in range(0,len(dataWarehouse.category.unique())):
#     categoryCount.append(len(dataWarehouse[dataWarehouse["category"] == dataWarehouse.category.unique()[x]]))

# categoryCount.pop(10)

# print(categoryCount)

# print(len(dataWarehouse[dataWarehouse["comments_disabled"] == True]))


# dislikesGreaterThanlikes = pd.DataFrame(dataWarehouse, columns=["likes","dislikes","comments_disabled","ratings_disabled"])

# dislikesGreaterThanlikes = dislikesGreaterThanlikes[dislikesGreaterThanlikes["dislikes"] > dislikesGreaterThanlikes["likes"]]

# print(len(dislikesGreaterThanlikes))


# print(type(dataWarehouse["trending_date"][0]))

# print(dataWarehouse["publish_time"][0])
# print(dataWarehouse["trending_date"][0])

# print(dataWarehouse["publish_time"][0][:10])
# print(dataWarehouse["trending_date"][0])
# deneme1 = re.sub("-","/",dataWarehouse["publish_time"][0][:10])
# deneme2 = re.sub('"\.\"',"/",dataWarehouse["trending_date"][0])
# print(deneme1)
# print(deneme2)

# print(dataWarehouse)