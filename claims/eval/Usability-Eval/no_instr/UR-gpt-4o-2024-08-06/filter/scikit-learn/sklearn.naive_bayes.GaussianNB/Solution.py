from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np

# Create a toy dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Assume data is coming in batches for online learning
# Split the training data into chunks for partial_fit
chunk_size = 100
n_chunks = X_train.shape[0] // chunk_size

# Online training with partial_fit
for i in range(n_chunks):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    X_chunk, y_chunk = X_train[start:end], y_train[start:end]
    
    # Partial fitting the model incrementally
    gnb.partial_fit(X_chunk, y_chunk, classes=np.unique(y_train))

# Evaluate the model on the test data
accuracy = gnb.score(X_test, y_test)
print("Test accuracy:", accuracy)
