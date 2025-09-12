from sklearn.metrics import r2_score

# Pass in the actual target values and predicted values as arguments to the function
def r2_regression_score(y_true, y_pred):
    return r2_score(y_true, y_pred)
