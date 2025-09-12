
from sklearn.metrics import explained_variance_score
# Assuming you have already fit your model to your data
y_true = ... # your true target values
y_pred = ... # your predicted target values
score = explained_variance_score(y_true, y_pred)
print(score)
