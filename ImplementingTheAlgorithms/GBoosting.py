import pandas as pd
import PerformanceMetrics as performanceMetrics
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix

processedDatas = pd.read_csv("../processedDataset.csv")[["video_id","trending_date","title","channel_title","category","category_id","publish_time","tags","views","likes",
"dislikes","comment_count",
"comments_disabled","ratings_disabled","video_error_or_removed","country_abb", "views_scaled", "likes_scaled", "dislikes_scaled", "comment_count_scaled", "music_cat", 
"comedy_cat","entertainment_cat", "news&politics_cat", "people&blogs_cat", "howto&style_cat", "film&animation_cat", "science&technology_cat", "gaming_cat", "sports_cat",
"pets&animals_cat", "travel&events_cat", "autos&vehicles_cat", "education_cat", "shows_cat", "movies_cat", "trailers_cat", "ca_country", "de_country", "fr_country",
"gb_country", "in_country", "jp_country", "kr_country", "mx_country", "ru_country","us_country"
]]


#region Verilen view sayısına gore videonun entertainment kategorisine ait olup olmadığını buluyor.

model = GradientBoostingClassifier()

predictionViews = processedDatas[["views"]]
predictionViews = predictionViews.values

predictionCat = processedDatas[["entertainment_cat"]]
predictionCat = predictionCat.values

from sklearn.model_selection import KFold
X = predictionViews
y = predictionCat
kf = KFold(n_splits=10)

predictions = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    predictions.append(model.predict(X_test))


bestResult = 0
bestConfusion = []

for prediction in predictions:
    confusionMatrix = confusion_matrix(y_test, prediction)
    accuracyScore = performanceMetrics.accuracy(confusionMatrix)
    if(accuracyScore > bestResult):
        bestResult = accuracyScore
        bestConfusion = confusionMatrix


# Metrics for entertainment category prediction
accuracyScore = performanceMetrics.accuracy(bestConfusion)
print("entertainmentViewsPrediction / Accuracy Score: {}".format(round(accuracyScore, 3)))

precisionScore = performanceMetrics.precision(bestConfusion)
print("entertainmentViewsPrediction / Precision Score: {}".format(round(precisionScore, 3)))

recallScore = performanceMetrics.recall(bestConfusion)
print("entertainmentViewsPrediction / Recall Score: {}".format(round(recallScore, 3)))

fMeasureScore = performanceMetrics.fmeasure(bestConfusion)
print("entertainmentViewsPrediction / F-Mesaure Score: {}".format(round(fMeasureScore, 3)))

#endregion


#region Verilen view sayısına gore videonun lokasyonunun US olup olmadığını buluyor.

model = GradientBoostingClassifier()

predictionViews = processedDatas[["views"]]
predictionViews = predictionViews.values

predictionUS = processedDatas[["us_country"]]
predictionUS = predictionUS.values

from sklearn.model_selection import KFold
X = predictionViews
y = predictionUS
kf = KFold(n_splits=10)

predictions = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    predictions.append(model.predict(X_test))


bestResult = 0
bestConfusion = []

for prediction in predictions:
    confusionMatrix = confusion_matrix(y_test, prediction)
    accuracyScore = performanceMetrics.accuracy(confusionMatrix)
    if(accuracyScore > bestResult):
        bestResult = accuracyScore
        bestConfusion = confusionMatrix


# Metrics for entertainment category prediction
accuracyScore = performanceMetrics.accuracy(bestConfusion)
print("entertainmentViewsPrediction / Accuracy Score: {}".format(round(accuracyScore, 3)))

precisionScore = performanceMetrics.precision(bestConfusion)
print("entertainmentViewsPrediction / Precision Score: {}".format(round(precisionScore, 3)))

recallScore = performanceMetrics.recall(bestConfusion)
print("entertainmentViewsPrediction / Recall Score: {}".format(round(recallScore, 3)))

fMeasureScore = performanceMetrics.fmeasure(bestConfusion)
print("entertainmentViewsPrediction / F-Mesaure Score: {}".format(round(fMeasureScore, 3)))

#endregion