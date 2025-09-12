
from sklearn.naive_bayes import GaussianNB
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB()
for i in range(X.shape[0]):
 clf.partial_fit(X[i].reshape(1, -1), y[i], np.unique(y)[i])
