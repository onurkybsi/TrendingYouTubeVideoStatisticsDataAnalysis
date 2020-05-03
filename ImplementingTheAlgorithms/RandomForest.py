import pandas as pd
import PerformanceMetrics as performanceMetrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

processedDatas = pd.read_csv("../processedDataset.csv")[["video_id","trending_date","title","channel_title","category","category_id","publish_time","tags","views","likes",
"dislikes","comment_count",
"comments_disabled","ratings_disabled","video_error_or_removed","country_abb", "views_scaled", "likes_scaled", "dislikes_scaled", "comment_count_scaled", "music_cat", 
"comedy_cat","entertainment_cat", "news&politics_cat", "people&blogs_cat", "howto&style_cat", "film&animation_cat", "science&technology_cat", "gaming_cat", "sports_cat",
"pets&animals_cat", "travel&events_cat", "autos&vehicles_cat", "education_cat", "shows_cat", "movies_cat", "trailers_cat", "ca_country", "de_country", "fr_country",
"gb_country", "in_country", "jp_country", "kr_country", "mx_country", "ru_country","us_country"
]]


# Verilen view sayısına gore videonun entertainment kategorisine ait olup olmadığını buluyor.

entertainmentViewsPrediction = processedDatas[["views", "entertainment_cat"]]

X_train, X_test, y_train, y_test = train_test_split(entertainmentViewsPrediction[["views"]], entertainmentViewsPrediction.entertainment_cat, train_size=0.8)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

# Confusion Matrix
confusionMatrix = confusion_matrix(y_test, predictions)
print("entertainmentViewsPrediction / Confusion Matrix:")
print(confusionMatrix)

# Metrics for entertainment category prediction
accuracyScore = performanceMetrics.accuracy(confusionMatrix)
print("entertainmentViewsPrediction / Accuracy Score: {}".format(round(accuracyScore, 3)))

precisionScore = performanceMetrics.precision(confusionMatrix)
print("entertainmentViewsPrediction / Precision Score: {}".format(round(precisionScore, 3)))

recallScore = performanceMetrics.recall(confusionMatrix)
print("entertainmentViewsPrediction / Recall Score: {}".format(round(recallScore, 3)))

fMeasureScore = performanceMetrics.fmeasure(confusionMatrix)
print("entertainmentViewsPrediction / F-Mesaure Score: {}".format(round(fMeasureScore, 3)))




# Verilen view sayısına gore videonun lokasyonunun US olup olmadığını buluyor.

usViewsPrediction = processedDatas[["views", "us_country"]]

X_train, X_test, y_train, y_test = train_test_split(usViewsPrediction[["views"]], usViewsPrediction.us_country, train_size=0.8)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)



# Confusion Matrix
confusionMatrix = confusion_matrix(y_test, predictions)
print("usViewsPrediction / Confusion Matrix:")
print(confusionMatrix)

# Metrics for US location prediction
accuracyScore = performanceMetrics.accuracy(confusionMatrix)
print("usViewsPrediction / Accuracy Score: {}".format(round(accuracyScore, 3)))

precisionScore = performanceMetrics.precision(confusionMatrix)
print("usViewsPrediction / Precision Score: {}".format(round(precisionScore, 3)))

recallScore = performanceMetrics.recall(confusionMatrix)
print("usViewsPrediction / Recall Score: {}".format(round(recallScore, 3)))

fMeasureScore = performanceMetrics.fmeasure(confusionMatrix)
print("usViewsPrediction / F-Mesaure Score: {}".format(round(fMeasureScore, 3)))