
from sklearn import metrics
import numpy as np

# Function to calculate the R2 score
def r2_score(y_true, y_pred):
    SS_res = np.sum((y_true - y_pred) ** 2)
    SS_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - SS_res / (SS_tot + np.finfo(float).eps)
