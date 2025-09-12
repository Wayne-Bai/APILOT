
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np
from scipy.spatial import distance

class RadiusNeighborsClassifier(BaseEstimator, ClassifierMixin):
    
    def __init__(self, radius=1.0):
        self.radius = radius
        
    def fit(self, X, y):
        self.X = X
        self.y = y
        
    def predict(self, X):
        y_pred = []
        for x in X:
            neighbors = [idx for idx, xi in enumerate(self.X) if distance.euclidean(xi, x) <= self.radius]
            if neighbors:
                neighbor_labels = [self.y[n] for n in neighbors]
                unique_labels, counts = np.unique(neighbor_labels, return_counts=True)
                y_pred.append(unique_labels[np.argmax(counts)])
            else:
                y_pred.append(None)
        return np.array(y_pred)
