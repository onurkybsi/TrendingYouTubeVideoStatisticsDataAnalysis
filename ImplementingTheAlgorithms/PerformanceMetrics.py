# Classification Rate/Accuracy:
# Accuracy = (TP + TN) / (TP + TN + FP + FN)
def accuracy(confusion_matrix):
    diagonal_sum = confusion_matrix.trace()
    sum_of_all_elements = confusion_matrix.sum()
    return diagonal_sum / sum_of_all_elements 


# Precision: Precsion tells us about when it predicts yes, how often is it correct.
# Precision = TP / (TP + FP)
def precision(confusion_matrix):
    positive_sum = confusion_matrix[0].sum()
    return (confusion_matrix[0][0]) / positive_sum


# Recall: Recall gives us an idea about when it’s actually yes, how often does it predict yes.
# Recall = TP / (TP + FN)
def recall(confusion_matrix):
    first_column_cum = confusion_matrix[0][0] + confusion_matrix[1][0]
    return (confusion_matrix[0][0]) / first_column_cum


# F-measure:
# Fmeasure = (2 * Recall * Precision) / (Recall + Presision)
def fmeasure(confusion_matrix):
    recallScore = recall(confusion_matrix)
    precisionScore = precision(confusion_matrix)
    return (2 * recallScore * precisionScore) / (recallScore + precisionScore)
