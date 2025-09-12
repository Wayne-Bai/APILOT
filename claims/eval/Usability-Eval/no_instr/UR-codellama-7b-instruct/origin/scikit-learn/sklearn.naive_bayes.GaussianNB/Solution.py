
from sklearn.naive_bayes import GaussianNB
import numpy as np

# create dataset for demonstration purposes
X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

# initialize Gaussian Naive Bayes classifier with Gamma prior
gnb = GaussianNB(prior='gamma')

# train model on dataset
gnb.fit(X, y)

# predict for new data
new_data = np.array([[3, 3]])
prediction = gnb.predict(new_data)
print(prediction)

# partial update of the model with new data
new_data = np.array([[4, 4]])
gnb.partial_fit(new_data)
