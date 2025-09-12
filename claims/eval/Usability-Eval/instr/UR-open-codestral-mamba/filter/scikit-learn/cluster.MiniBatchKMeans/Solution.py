# Import necessary libraries
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import load_digits
import numpy as np

# Load the dataset
digits = load_digits()
data = digits.images.reshape((len(digits.images), -1))

# Define the model
model = MiniBatchKMeans(n_clusters=10, random_state=0, batch_size=64)

# Fit the model to the data
model.fit(data)

# Predict the cluster each data point belongs to
labels = model.predict(data)

# Check the size of the labels array should match the number of data points
print('Number of data points:', len(labels))
