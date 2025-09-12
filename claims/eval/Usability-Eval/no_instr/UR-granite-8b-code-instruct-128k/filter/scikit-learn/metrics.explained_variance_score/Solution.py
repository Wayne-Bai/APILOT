
from sklearn.metrics import explained_variance_score
import numpy as np

# Generate some example data
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 2.2, 3.1, 4.1, 5.2])

# Calculate the explained variance regression score
score = explained_variance_score(y_true, y_pred)

# Print the result
print("Explained variance regression score:", score)
