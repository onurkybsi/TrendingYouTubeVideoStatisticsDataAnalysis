import csv
import pandas as pd
import json

CAvideosDatas = pd.read_csv("Dataset/CAvideos.csv")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

CAvideosDatas["country_abb"] = "CA"

DEvideosDatas = pd.read_csv("Dataset/DEvideos.csv")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

DEvideosDatas["country_abb"] = "DE"

FRvideosDatas = pd.read_csv("Dataset/FRvideos.csv")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

FRvideosDatas["country_abb"] = "FR"

GBvideosDatas = pd.read_csv("Dataset/GBvideos.csv")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

GBvideosDatas["country_abb"] = "GB"

INvideosDatas = pd.read_csv("Dataset/INvideos.csv")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

INvideosDatas["country_abb"] = "IN"

JPvideosDatas = pd.read_csv("Dataset/JPvideos.csv",encoding="latin1")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

JPvideosDatas["country_abb"] = "JP"

KRvideosDatas = pd.read_csv("Dataset/KRvideos.csv",encoding="latin1")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

KRvideosDatas["country_abb"] = "KR"

MXvideosDatas = pd.read_csv("Dataset/MXvideos.csv",encoding="latin1")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

MXvideosDatas["country_abb"] = "MX"

RUvideosDatas = pd.read_csv("Dataset/RUvideos.csv",encoding="latin1")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

RUvideosDatas["country_abb"] = "RU"

USvideosDatas = pd.read_csv("Dataset/USvideos.csv")[["video_id","trending_date","title","channel_title","category_id","publish_time","tags","views","likes","dislikes","comment_count",
"thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"]]

USvideosDatas["country_abb"] = "US"

dataWarehouse = pd.concat([CAvideosDatas,DEvideosDatas,FRvideosDatas,GBvideosDatas, INvideosDatas,JPvideosDatas,KRvideosDatas,MXvideosDatas,RUvideosDatas,USvideosDatas], ignore_index=True)

dataWarehouse["category_id"] = dataWarehouse["category_id"].astype(str)

category_id = {}

with open("category_info.json", "r") as f:
    category_info = json.load(f)
    for category in category_info["items"]:
        category_id[category["id"]] = category["snippet"]["title"]


dataWarehouse.insert(4, "category", dataWarehouse["category_id"].map(category_id))

# dataWarehouse.to_csv(r'C:\Users\onurb\Source\Arastirma\arrangedDataset.csv')