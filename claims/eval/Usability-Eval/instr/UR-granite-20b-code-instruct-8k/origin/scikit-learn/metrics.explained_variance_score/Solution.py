
from sklearn.metrics import r2_score
import numpy as np

# Assuming you have the actual and predicted values stored in the variables y_actual and y_predicted
y_actual = np.array([1, 2, 3, 4, 5])
y_predicted = np.array([1.1, 1.9, 3.2, 4.1, 4.9])

# Calculate the explained variance regression score
score = r2_score(y_actual, y_predicted)
print("Explained variance regression score: ", score)
