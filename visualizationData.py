import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sn



dataWarehouse = pd.read_csv("arrangedDataset.csv")[["video_id","trending_date","title","channel_title","category","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","country_abb"]]

# First 100 data

# print(dataWarehouse.head(100))


# RelationBetweenVideoIdAndViews

# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["views"])
# plt.xlabel("Video Id")
# plt.ylabel("Views")
# plt.title("Relation between video id and views")
# plt.show()


# RelationBetweenVideoIdAndLikes

# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["likes"])
# plt.xlabel("Video Id")
# plt.ylabel("Likes")
# plt.title("Relation between video id and likes")
# plt.show()


# RelationBetweenVideoIdAndDislikes

# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["dislikes"])
# plt.xlabel("Video Id")
# plt.ylabel("Dislikes")
# plt.title("Relation between video id and dislikes")
# plt.show()


# RelationBetweenVideoIdAndCommenCount

# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["comment_count"])
# plt.xlabel("Video Id")
# plt.ylabel("Comment Count")
# plt.title("Relation between video id and comment count")
# plt.show()


# Finding views relative to country

# CAviews = 0
# DEviews = 0
# FRviews = 0
# GBviews = 0
# INviews = 0
# JPviews = 0
# KRviews = 0
# MXviews = 0
# RUviews = 0
# USviews = 0

# for x in range(0,375942):
#     if(dataWarehouse["country_abb"][x] == "CA"):
#         CAviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "DE"):
#         DEviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "FR"):
#         FRviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "GB"):
#         GBviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "IN"):
#         INviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "JP"):
#         JPviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "KR"):
#         KRviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "MX"):
#         MXviews += dataWarehouse["views"][x]
#     elif(dataWarehouse["country_abb"][x] == "RU"):
#         RUviews += dataWarehouse["views"][x]
#     else:
#         USviews += dataWarehouse["views"][x]

# trendRelativeToCountry = [CAviews,DEviews,FRviews,GBviews,INviews,JPviews,KRviews,MXviews,RUviews,USviews]

# print(trendRelativeToCountry)

# RelationBetweenViewsCountry

# trendRelativeToCountry = [46891975069, 24645115205, 17100897444, 230069198174, 39610961029, 5377466630, 14689152313, 13849692994, 9806494525, 96671770152]
# plt.pie(trendRelativeToCountry, labels=["CA","DE","FR","GB","IN","JP","KR","MX","RU","US"], wedgeprops={'edgecolor':'black'}, explode=[0,0,0,0,0,0.3,0.1,0.1,0.2,0], shadow=True, autopct="%1.1f%%")
# plt.title("Relation Between Views Country")
# plt.show()
