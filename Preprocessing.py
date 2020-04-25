import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import MinMaxScaler

missingValues = ["n/a", "na", "null", -1, "none", "?","-", "/",None,"None","none","NaN","nan"]

dataWarehouse = pd.read_csv("arrangedDataset.csv", na_values = missingValues)
[["video_id","trending_date","title","channel_title","category",
"category_id","publish_time","tags","views","likes","dislikes","comment_count","thumbnail_link","comments_disabled",
"ratings_disabled","video_error_or_removed","description","country_abb"]]


# Detecting NaN values


# NaN value counts
print(dataWarehouse.isnull().sum())
print("\n")


# Inf value control of Int types
for column in dataWarehouse:
    if(type(dataWarehouse[column][0]) == np.int64):
        if(np.isposinf(dataWarehouse[column]).any() or np.isneginf(dataWarehouse[column]).any()):
            print("Yes, there are inf values in " + column)
        else:
            print("No, inf values in" + column)

print("\n")




# Dropping "thumbnail_link" and "description" columns
dataWarehouse.drop(columns = ['thumbnail_link'], axis = 1, inplace = True)
dataWarehouse.drop(columns = ['description'], axis = 1, inplace = True)




# Calculation of the frequencies of the category column
categories = list(dataWarehouse.category.unique())
categories.pop(10)

categoryPercentages = []

for x in range(0,len(dataWarehouse.category.unique())):
    if x != 10:
        categoryPercentages.append(int((len(dataWarehouse[dataWarehouse["category"] == dataWarehouse.category.unique()[x]])/373147*2795)))

print(categories)
print(categoryPercentages)




# Filling null values of the category column

index = 0

for y in range(0, len(dataWarehouse["category"])):
    if pd.isnull(dataWarehouse["category"][y]):
        if index < 318:
            dataWarehouse.iat[y, 5] = "Music"
            index = index + 1
        elif 318 <= index < 520:
            dataWarehouse.iat[y, 5] = "Comedy"
            index = index + 1
        elif 520 <= index < 1336:
            dataWarehouse.iat[y, 5] = "Entertainment"
            index = index + 1
        elif 1336 <= index < 1615:
            dataWarehouse.iat[y, 5] = "News & Politics"
            index = index + 1
        elif 1615 <= index < 2019:
            dataWarehouse.iat[y, 5] = "People & Blogs"
            index = index + 1
        elif 2019 <= index < 2160:
            dataWarehouse.iat[y, 5] = "Howto & Style"
            index = index + 1
        elif 2160 <= index < 2316:
            dataWarehouse.iat[y, 5] = "Film & Animation"
            index = index + 1
        elif 2316 <= index < 2377:
            dataWarehouse.iat[y, 5] = "Science & Technology"
            index = index + 1
        elif 2377 <= index < 2463:
            dataWarehouse.iat[y, 5] = "Gaming"
            index = index + 1
        elif 2463 <= index < 2640:
            dataWarehouse.iat[y, 5] = "Sports"
            index = index + 1
        elif 2640 <= index < 2676:
            dataWarehouse.iat[y, 5] = "Pets & Animals"
            index = index + 1
        elif 2676 <= index < 2689:
            dataWarehouse.iat[y, 5] = "Travel & Events"
            index = index + 1
        elif 2689 <= index < 2724:
            dataWarehouse.iat[y, 5] = "Autos & Vehicles"
            index = index + 1
        elif 2724 <= index < 2782:
            dataWarehouse.iat[y, 5] = "Education"
            index = index + 1
        elif 2782 <= index < 2789:
            dataWarehouse.iat[y, 5] = "Shows"
            index = index + 1
        elif 2789 <= index < 2792:
            dataWarehouse.iat[y, 5] = "Movies"
            index = index + 1
        elif 2792 <= index < 2795:
            dataWarehouse.iat[y, 5] = "Trailers"
            index = index + 1


print(dataWarehouse.isnull().sum())
print("\n")




# Anomalies on rates of likes and dislikes
requiredData = pd.DataFrame(dataWarehouse, columns=["likes","dislikes"])
requiredData["rate"] = (requiredData["likes"] / requiredData["dislikes"])
requiredData = requiredData[requiredData["rate"] != float("inf")]
print("Anomalies of rates of likes and dislikes " + str(len(requiredData[requiredData["rate"] > 1000])) + "\n")

# Arragement on rates of likes and dislikes
dataWarehouse.drop(dataWarehouse[(dataWarehouse.likes/dataWarehouse.dislikes) > 1000].index, inplace = True)

requiredData = pd.DataFrame(dataWarehouse, columns=["likes","dislikes"])
requiredData["rate"] = (requiredData["likes"] / requiredData["dislikes"])
requiredData = requiredData[requiredData["rate"] != float("inf")]
print("Anomalies of rates of likes and dislikes " + str(len(requiredData[requiredData["rate"] > 1000])) + "\n")




# Other numerical anomalies
print("Anomalies of relation between video id and views " + str(len(dataWarehouse[dataWarehouse["views"] > 9000000])))
print("Anomalies of relation between video id and likes " + str(len(dataWarehouse[dataWarehouse["likes"] > 300000])))
print("Anomalies of relation between video id and dislikes " + str(len(dataWarehouse[dataWarehouse["dislikes"] > 14000])))
print("Anomalies of relation between video id and comment count " + str(len(dataWarehouse[dataWarehouse["comment_count"] > 30000])) + "\n")




# Arrangement of views anomalies
meanViews = int(np.mean(dataWarehouse["views"]))
print("Mean value of views : " + str(meanViews) + "\n")
dataWarehouse["views"] = np.where(dataWarehouse["views"] > 9000000, meanViews,dataWarehouse["views"])

# After arrangement
# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["views"])
# plt.xlabel("Video Id")
# plt.ylabel("Views")
# plt.title("Relation between video id and views")
# plt.show()




# Arrangement of likes anomalies
meanLikes = int(np.mean(dataWarehouse["likes"]))
print("Mean value of likes : " + str(meanLikes) + "\n")
dataWarehouse["likes"] = np.where(dataWarehouse["likes"] > 300000, meanLikes, dataWarehouse["likes"])

# After arrangement
# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["likes"])
# plt.xlabel("Video Id")
# plt.ylabel("Likes")
# plt.title("Relation between video id and likes")
# plt.show()




# Arrangement of dislikes anomalies
meanDislikes = int(np.mean(dataWarehouse["dislikes"]))
print("Mean value of likes : " + str(meanDislikes) + "\n")
dataWarehouse["dislikes"] = np.where(dataWarehouse["dislikes"] > 14000, meanDislikes, dataWarehouse["dislikes"])

# After arrangement
# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["dislikes"])
# plt.xlabel("Video Id")
# plt.ylabel("Dislikes")
# plt.title("Relation between video id and dislikes")
# plt.show()




# Arrangement of comment count anomalies
meanCommentCount = int(np.mean(dataWarehouse["comment_count"]))
print("Mean value of comment count : " + str(meanCommentCount) + "\n")
dataWarehouse["comment_count"] = np.where(dataWarehouse["comment_count"] > 30000, meanCommentCount, dataWarehouse["comment_count"])

# After arrangement
# plt.scatter(dataWarehouse["video_id"].index.values.astype(int),dataWarehouse["comment_count"])
# plt.xlabel("Video Id")
# plt.ylabel("Comment Count")
# plt.title("Relation between video id and comment count")
# plt.show()




# Min-max normalization for numerical colums

scaler = MinMaxScaler()

dataWarehouse["views_scaled"] = 0
dataWarehouse["likes_scaled"] = 0
dataWarehouse["dislikes_scaled"] = 0
dataWarehouse["comment_count_scaled"] = 0

dataWarehouse[["views_scaled", "likes_scaled", "dislikes_scaled", "comment_count_scaled"]] = scaler.fit_transform(dataWarehouse[["views", "likes", "dislikes", "comment_count"]])



# Dummy value assignment for the categorical columns

for x in dataWarehouse["category"].unique():
    columnName = x.lower().replace(" ", "") + "_cat"
    dataWarehouse[columnName] = pd.get_dummies(dataWarehouse["category"])[x]

for x in dataWarehouse["country_abb"].unique():
    columnName = x.lower().replace(" ", "") + "_country"
    dataWarehouse[columnName] = pd.get_dummies(dataWarehouse["country_abb"])[x]

pd.options.display.max_columns = None
pd.options.display.max_rows = None

print(dataWarehouse.head(20))
