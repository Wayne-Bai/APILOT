
import pandas as pd
from sklearn.metrics import confusion_matrix

# Load your data into a Pandas DataFrame
y_true = ... # true labels
y_pred = ... # predicted labels

# Generate the confusion matrix using scikit-learn's confusion_matrix() function
conf_mat = confusion_matrix(y_true, y_pred)

# Print or visualize the confusion matrix
print(conf_mat)
