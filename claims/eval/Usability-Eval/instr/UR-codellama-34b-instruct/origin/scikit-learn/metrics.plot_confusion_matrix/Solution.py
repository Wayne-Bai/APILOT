
import numpy as np
from sklearn.metrics import confusion_matrix

# Load your dataset
X = ...
y = ...

# Train your model on the data
model = ...

# Use the confusion matrix function to get the confusion matrix
conf_mat = confusion_matrix(y, model.predict(X))

# Print the confusion matrix
print(conf_mat)
