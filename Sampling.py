import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import KFold
import ImplementingTheAlgorithms.PerformanceMetrics as performanceMetrics
import random


processedDatas = pd.read_csv("./processedDataset.csv")[["video_id","trending_date","title","channel_title","category","category_id","publish_time","tags","views","likes",
"dislikes","comment_count",
"comments_disabled","ratings_disabled","video_error_or_removed","country_abb", "views_scaled", "likes_scaled", "dislikes_scaled", "comment_count_scaled", "music_cat", 
"comedy_cat","entertainment_cat", "news&politics_cat", "people&blogs_cat", "howto&style_cat", "film&animation_cat", "science&technology_cat", "gaming_cat", "sports_cat",
"pets&animals_cat", "travel&events_cat", "autos&vehicles_cat", "education_cat", "shows_cat", "movies_cat", "trailers_cat", "ca_country", "de_country", "fr_country",
"gb_country", "in_country", "jp_country", "kr_country", "mx_country", "ru_country","us_country"
]]

sample_df = processedDatas.sample(10000)

modelDecisionTreeClassifier = DecisionTreeClassifier()
modelGradientBoostingClassifier = GradientBoostingClassifier()
modelLogisticRegression = LogisticRegression()
modelRandomForestClassifier = RandomForestClassifier()

models = [[modelDecisionTreeClassifier, modelGradientBoostingClassifier, modelLogisticRegression, modelRandomForestClassifier],
           ["Decision Tree", "GBoosting", "Logistic Regression", "Random Forest"],
           ["Entertainment category prediction", "US location prediction"]]

predictionViews = sample_df[["views"]].to_numpy()

predictionCat = sample_df[["entertainment_cat"]].to_numpy()

predictionUS = sample_df[["us_country"]].to_numpy()

X = predictionViews
kf = KFold(n_splits=10,shuffle=False)

bestResult = 0
bestConfusion = []

i = 0
for model in models[0]:
    y = predictionCat
    for j in range(2):
        print("For {prediction}, {algorithm} algorithm:".format(prediction = models[2][j] , algorithm = models[1][i]))
        for train_index, test_index in kf.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            model.fit(X_train, y_train.ravel())
            prediction = model.predict(X_test)
            confusionMatrix = confusion_matrix(y_test, prediction)
            accuracyScore = performanceMetrics.accuracy(confusionMatrix)
            if(accuracyScore > bestResult):
                bestResult = accuracyScore
                bestConfusion = confusionMatrix

        # Metrics for entertainment category predictio
        accuracyScore = performanceMetrics.accuracy(bestConfusion)
        print("Accuracy Score: {}".format(round(accuracyScore, 3)))

        precisionScore = performanceMetrics.precision(bestConfusion)
        print("Precision Score: {}".format(round(precisionScore, 3)))

        recallScore = performanceMetrics.recall(bestConfusion)
        print("Recall Score: {}".format(round(recallScore, 3)))

        fMeasureScore = performanceMetrics.fmeasure(bestConfusion)
        print("F-Mesaure Score: {}".format(round(fMeasureScore, 3)))
        bestResult = 0      
        bestConfusion = []
        print("\n")
        y = predictionUS
    i = i + 1


