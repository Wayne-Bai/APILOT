
import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin

class CustomClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, *args, **kwargs):
        self.model = tf.keras.Sequential(*args, **kwargs)
    
    def fit(self, X, y):
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(X, y, epochs=10)
        
    def predict(self, X):
        predictions = self.model.predict(X)
        return predictions.argmax(axis=1)
