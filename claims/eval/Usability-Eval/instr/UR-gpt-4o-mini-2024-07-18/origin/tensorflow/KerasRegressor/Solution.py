import tensorflow as tf
from sklearn.base import ClassifierMixin

class TensorFlowClassifier(ClassifierMixin):
    def __init__(self, model=None, epochs=10, batch_size=32):
        self.model = model
        self.epochs = epochs
        self.batch_size = batch_size

    def fit(self, X, y):
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size)

    def predict(self, X):
        return tf.argmax(self.model(X), axis=1)

    def score(self, X, y):
        return self.model.evaluate(X, y, verbose=0)[1]
