import pandas as pd
import PerformanceMetrics as performanceMetrics
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


processedDatas = pd.read_csv("../processedDataset.csv")[["video_id","trending_date","title","channel_title","category","category_id","publish_time","tags","views","likes",
"dislikes","comment_count",
"comments_disabled","ratings_disabled","video_error_or_removed","country_abb", "views_scaled", "likes_scaled", "dislikes_scaled", "comment_count_scaled", "music_cat", 
"comedy_cat","entertainment_cat", "news&politics_cat", "people&blogs_cat", "howto&style_cat", "film&animation_cat", "science&technology_cat", "gaming_cat", "sports_cat",
"pets&animals_cat", "travel&events_cat", "autos&vehicles_cat", "education_cat", "shows_cat", "movies_cat", "trailers_cat", "ca_country", "de_country", "fr_country",
"gb_country", "in_country", "jp_country", "kr_country", "mx_country", "ru_country","us_country"
]]


predictionViews = processedDatas[["views"]].to_numpy()

predictionCat = processedDatas[["entertainment_cat"]].to_numpy()

predictionUS = processedDatas[["us_country"]].to_numpy()

#region Verilen view sayısına gore videonun entertainment kategorisine ait olup olmadığını buluyor.

modelUS = LogisticRegression()

X = predictionViews
y = predictionCat
kf = KFold(n_splits=10,shuffle=False)

bestResult = 0
bestConfusion = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    modelUS.fit(X_train, y_train.ravel())
    prediction = modelUS.predict(X_test)
    confusionMatrix = confusion_matrix(y_test, prediction)
    accuracyScore = performanceMetrics.accuracy(confusionMatrix)
    if(accuracyScore > bestResult):
        bestResult = accuracyScore
        bestConfusion = confusionMatrix    

ax = plt.axes()
sns.heatmap(bestConfusion, annot=True, fmt="d", ax=ax)
ax.set_title("Accuracy score for Entertainment category prediction: {}".format(round(bestResult, 3)))
plt.show()

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

modelUS = LogisticRegression()

X = predictionViews
y = predictionUS
kf = KFold(n_splits=10,shuffle=False)

bestResult = 0
bestConfusion = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    modelUS.fit(X_train, y_train.ravel())
    prediction = modelUS.predict(X_test)
    confusionMatrix = confusion_matrix(y_test, prediction)
    accuracyScore = performanceMetrics.accuracy(confusionMatrix)
    if(accuracyScore > bestResult):
        bestResult = accuracyScore
        bestConfusion = confusionMatrix    


ax = plt.axes()
sns.heatmap(bestConfusion, annot=True, fmt="d", ax=ax)
ax.set_title("Accuracy score for US location prediction: {}".format(round(bestResult, 3)))
plt.show()

# Metrics for entertainment category prediction
accuracyScore = performanceMetrics.accuracy(bestConfusion)
print("USViewsPrediction / Accuracy Score: {}".format(round(accuracyScore, 3)))

precisionScore = performanceMetrics.precision(bestConfusion)
print("USViewsPrediction / Precision Score: {}".format(round(precisionScore, 3)))

recallScore = performanceMetrics.recall(bestConfusion)
print("USViewsPrediction / Recall Score: {}".format(round(recallScore, 3)))

fMeasureScore = performanceMetrics.fmeasure(bestConfusion)
print("USViewsPrediction / F-Mesaure Score: {}".format(round(fMeasureScore, 3)))

#endregion